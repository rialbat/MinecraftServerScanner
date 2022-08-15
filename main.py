#F:\Visual Studio Shared\Python39_64

# For reqs and resps
import socket
import requests

# Pack data
import struct

import json
import sys
import time
import ipaddress
import re

# For Multithreading
from concurrent.futures import ThreadPoolExecutor

# GUI
from PySide6 import QtWidgets, QtCore, QtGui
import MainWindow

#GEO
from findGEO import FindGEO

programVersion = '0.5'


class ServerStatus:
    def __init__(self, host='127.0.0.1', port=25565, timeout=2):
        self._host = host
        self._port = port
        self._timeout = timeout

    def _unpack_varint(self, sock):
        data = 0
        for i in range(5):
            ordinal = sock.recv(1)

            if len(ordinal) == 0:
                break

            byte = ord(ordinal)
            data |= (byte & 0x7F) << 7 * i

            if not byte & 0x80:
                break

        return data

    def _pack_varint(self, data):
        ordinal = b''

        while True:
            byte = data & 0x7F
            data >>= 7
            ordinal += struct.pack('B', byte | (0x80 if data > 0 else 0))

            if data == 0:
                break

        return ordinal

    def _pack_data(self, data):
        if type(data) is str:
            data = data.encode('utf8')
            return self._pack_varint(len(data)) + data
        elif type(data) is int:
            return struct.pack('H', data)
            # Return a bytes object containing the values
            # packed according to the format string format.
        elif type(data) is float:
            return struct.pack('Q', int(data))
        else:
            return data

    def _send_data(self, connection, *args):
        data = b''

        for arg in args:
            data += self._pack_data(arg)

        connection.send(self._pack_varint(len(data)) + data)

    def _read_fully(self, connection, extra_varint=False):
        packet_length = self._unpack_varint(connection)
        packet_id = self._unpack_varint(connection)
        byte = b''

        if extra_varint:
            if packet_id > packet_length:
                self._unpack_varint(connection)

            extra_length = self._unpack_varint(connection)

            while len(byte) < extra_length:
                byte += connection.recv(extra_length)

        else:
            byte = connection.recv(packet_length)

        return byte
# Send Handshake:
    def get_status(self):
        # Create socket ipv4(AF_INET) for TCP(SOCK_STREAM)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection:
            connection.settimeout(self._timeout)
            connection.connect((self._host, self._port))
            '''
            Now we need to send packet with:
            1. Protocol version (minecraft client version (is not important for the ping)),
            2. Server Address,
            3. Server Port,
            4. Next stare (we should use "1" for status).
            '''
            self._send_data(connection, b'\x00\x00', self._host, self._port, b'\x01')

            # Now we need to send the status request (0x00 packet with no fields)
            self._send_data(connection, b'\x00')

            # Read response
            data = self._read_fully(connection, extra_varint=True)

            # Send and read unix time
            self._send_data(connection, b'\x01', time.time() * 1000)
            unix = self._read_fully(connection)
        # Load json and return
        response = json.loads(data.decode('utf8'))
        response['ping'] = int(time.time() * 1000) - struct.unpack('Q', unix)[0]

        response['ip'] = self._host
        response['port'] = self._port

        # Country, City
        try:
            gesGeo = FindGEO(self._host)
            gesGeo.findLocation()

            response['country'] = gesGeo.getCountry()
            response['city'] = gesGeo.getCity()

        except Exception:
            response['country'] = ''
            response['city'] = ''

        # Hostname
        try:
            response['host'] = socket.gethostbyaddr(self._host)[0]
        except Exception:
            response['host'] = ''

        return response

class Worker(QtCore.QRunnable):
    responseSignal = QtCore.Signal(str)
    def __init__(self, ip, port, timeout):
        super().__init__()
        self._ip = ip
        self._specificPort = port
        self._specificTimeOut = timeout

    @QtCore.Slot()
    def run(self):
        lServerStatus = ServerStatus(self._ip, self._specificPort, self._specificTimeOut)

        try:
            serverResponse = lServerStatus.get_status()
        except Exception:
            pass
        else:
            self.responseSignal.emit(serverResponse)


class ProgrammUI(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.menuAbout.customTriggeredSignal.connect(self.aboutMessage)
        self.startButton.clicked.connect(self.startAsyncSerch)
        self.stopButton.clicked.connect(self.stopAsyncSerch)
        self.pauseButton.clicked.connect(self.pauseAsyncSerch)
        self.actionSave_results.triggered.connect(self.saveResults)
        self.actionOpen_file.triggered.connect(self.openResults)

        workerClass = Worker
        workerClass.responseSignal[str].connect(self.receiveResponse)

        self._model = QtGui.QStandardItemModel()
        self.tableInit()

        self._start_ip = '127.0.0.1'
        self._end_ip = '127.0.0.1'
        self._specificPort = 25565
        self._specificTimeOut = 2
        self._curLine = 0
        self._totalLines = 0
        self._checked = 0
        self._threads = 0

        self._threadPool = QtCore.QThreadPool()

        self._serverResponseList = []

    @QtCore.Slot(str)
    def receiveResponse(self, response):
        self._serverResponseList.append(response)

    def tableInit(self):
        headersLabels = ["ID", "Server address", "Server description",
                         "Version", "Online", "Max players", "Country", "City",
                         "Hostname", "Ping"]

        self._model.setHorizontalHeaderLabels(headersLabels)
        self.tableView.setModel(self._model)

    def findDescription(self, serverResponse):
        pattern = r'\'text\': \'(.*?)\'}|\'description\': \'(.*?)\'|\'text\': \"(.*?)\"'
        subPattern = r'\\n|\\r| {2,}'
        secSubPattern = r'\\|§.|^[ ]'
        finalMatch = ''
        matches = re.finditer(pattern, str(serverResponse), re.MULTILINE)

        for matchNum, match in enumerate(matches, start=1):
            for groupNum in range(0, len(match.groups())):
                groupNum = groupNum + 1
                if match.group(groupNum) is not None:
                    finalMatch = finalMatch + match.group(groupNum)

        finalMatch = re.sub(subPattern, ' ', finalMatch)
        finalMatch = re.sub(secSubPattern, '', finalMatch)
        return finalMatch

    def saveResults(self):
        path = QtWidgets.QFileDialog.getSaveFileName(
            self, 'Save File', '', 'CSV(*.csv)')
        file = QtCore.QFile(path[0])
        if path[0]:
            if file.open(QtCore.QFile.WriteOnly | QtCore.QFile.Truncate):
                data = QtCore.QTextStream(file)
                strList = []
                for column in range(self._model.columnCount()):
                    if (len(str(self._model.headerData(column,
                    QtCore.Qt.Horizontal, QtCore.Qt.DisplayRole))) > 0): # type: ignore
                        strList.append(str(self._model.headerData(column,
                    QtCore.Qt.Horizontal, QtCore.Qt.DisplayRole))) # type: ignore
                    else:
                        strList.append('')
                data << ";".join(strList) << "\n"
                for row in range(self._model.rowCount()):
                    strList.clear()
                    for column in range(self._model.columnCount()):
                        if len(str(self._model.data(self._model.index(row, column)))) > 0:
                            strList.append(str(self._model.data(self._model.index(row, column))))
                        else:
                            strList.append("")
                    data << ";".join(strList) + "\n"
                QtWidgets.QMessageBox.information(self, "Save result",
                                        "Success!")

    def openResults(self):
        path = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Open File', '', 'CSV(*.csv)')
        file = QtCore.QFile(path[0])
        readHeaders = True
        if file.open(QtCore.QIODevice.ReadOnly): # type: ignore
            lineIndex = 0
            inStream = QtCore.QTextStream(file)
            while not inStream.atEnd():
                fileLine = inStream.readLine()
                lineToken = fileLine.split(";")
                if readHeaders:
                    readHeaders = False
                    continue
                for j in range(len(lineToken)):
                    curValue = lineToken[j]
                    item = QtGui.QStandardItem(curValue)
                    item.setTextAlignment(QtCore.Qt.AlignCenter) # type: ignore
                    self._model.setItem(lineIndex, j, item)
                lineIndex = lineIndex + 1
            self.tableView.resizeColumnsToContents()
            self.tableView.resizeRowsToContents()
            self.tableView.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.TextWordWrap)
            self.tableView.horizontalHeader().setMinimumHeight(40)


    def aboutMessage(self):
        QtWidgets.QMessageBox.about(self, "About",
                                    str("The program was created by rialbat\nVersion: %s\nMIT License" % programVersion))

    def showTableResult(self):
        self._model.removeRows(0, self._model.rowCount())
        lIndex = 0

        for result in self._serverResponseList:
            lIndex = lIndex + 1
            # ID
            itemID = QtGui.QStandardItem(str(lIndex))
            itemID.setTextAlignment(QtCore.Qt.AlignCenter)  # type: ignore
            self._model.setItem(lIndex - 1, 0, itemID)

            # Server address
            itemSAdd = QtGui.QStandardItem(str(result['ip']) + ":"
                                           + str(result['port']))
            itemSAdd.setTextAlignment(QtCore.Qt.AlignCenter)  # type: ignore
            self._model.setItem(lIndex - 1, 1, itemSAdd)

            # Server description
            currentDescription = self.findDescription(result)
            itemDesc = QtGui.QStandardItem(currentDescription)
            itemDesc.setTextAlignment(QtCore.Qt.AlignCenter)  # type: ignore
            self._model.setItem(lIndex - 1, 2, itemDesc)

            # Version
            try:
                itemVersion = QtGui.QStandardItem(str(result['version']['name']))
            except Exception:
                pass
            else:
                itemVersion.setTextAlignment(QtCore.Qt.AlignCenter)  # type: ignore
                self._model.setItem(lIndex - 1, 3, itemVersion)

            # Online, Max players
            try:
                itemOnline = QtGui.QStandardItem(str(result['players']['online']))
                itemMaxPlayers = QtGui.QStandardItem(str(result['players']['max']))
            except Exception:
                pass
            else:
                itemOnline.setTextAlignment(QtCore.Qt.AlignCenter)  # type: ignore
                itemMaxPlayers.setTextAlignment(QtCore.Qt.AlignCenter)  # type: ignore

                self._model.setItem(lIndex - 1, 4, itemOnline)
                self._model.setItem(lIndex - 1, 5, itemMaxPlayers)

            # Country, City, Hostname
            itemCountry = QtGui.QStandardItem(str(result['country']))
            itemCity = QtGui.QStandardItem(str(result['city']))
            itemHostname = QtGui.QStandardItem(str(result['host']))

            itemCountry.setTextAlignment(QtCore.Qt.AlignCenter)  # type: ignore
            itemCity.setTextAlignment(QtCore.Qt.AlignCenter)  # type: ignore
            itemHostname.setTextAlignment(QtCore.Qt.AlignCenter)  # type: ignore

            self._model.setItem(lIndex - 1, 6, itemCountry)
            self._model.setItem(lIndex - 1, 7, itemCity)
            self._model.setItem(lIndex - 1, 8, itemHostname)

            # Ping
            itemPing = QtGui.QStandardItem(str(result['ping']))
            itemPing.setTextAlignment(QtCore.Qt.AlignCenter)  # type: ignore
            self._model.setItem(lIndex - 1, 9, itemPing)

            self.actionSave_results.setEnabled(True)

            self.tableView.resizeColumnsToContents()
            self.tableView.resizeRowsToContents()
            self.tableView.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.TextWordWrap)
            self.tableView.horizontalHeader().setMinimumHeight(40)

    def updateStats(self):
        self.CheckedLabelStat.setText(str(self._checked))
        self.FoundLabelStat.setText(str(self._curLine))

    def startAsyncSerch(self):
        self.stopButton.setEnabled(True)
        self.pauseButton.setEnabled(True)
        self.pauseButton.setText("Pause")

        self._specificPort = self.portSpinBox.value()
        self._specificTimeOut = self.timeOutSpinBox.value()

        self._start_ip = ipaddress.IPv4Address(self.startIpLineEdit.text())
        self._end_ip = ipaddress.IPv4Address(self.endIpLineEdit.text())

        self._totalLines = (int(self._end_ip)+1) - int(self._start_ip)
        self.IPsLabelStat.setText(str(self._totalLines))

        self._threads = self.threadsSpinBox.value()
        ipPool = [] # TODO: Store Ips in parts

        for ip_int in range(int(self._start_ip), int(self._end_ip)+1):
            ipPool.append(str(ipaddress.IPv4Address(ip_int)))

        start_time = time.time()
        self._threadPool.setMaxThreadCount(self._threads)
        for ip in ipPool:
            self._threadPool.start(Worker(ip, self._specificPort, self._specificTimeOut))
            self._checked = self._checked + 1

        # self._serverResponseList = worker.getResult()

        self.updateStats()
        self.showTableResult()
        print("--- %s seconds ---" % (time.time() - start_time))

    def stopAsyncSerch(self):
        # TODO: stop actions
        self.stopButton.setEnabled(False)
        self.pauseButton.setEnabled(False)
        self.pauseButton.setText("Pause")

    def pauseAsyncSerch(self):
        self.pauseButton.setText("Resume")

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ProgrammUI()
    window.show()
    app.exec()
if __name__ == '__main__':
    main()
