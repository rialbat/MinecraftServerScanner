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

# GUI
from PySide6 import QtWidgets, QtCore, QtGui
import MainWindow

# Parse
#from bs4 import BeautifulSoup


class ServerStatus:
    def __init__(self, host='127.0.0.1', port=25565, timeout=5):
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

        return response

class ProgrammUI(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.menuAbout.customTriggeredSignal.connect(self.aboutMessage)
        self.startButton.clicked.connect(self.startAsyncSerch)
        self.stopButton.clicked.connect(self.stopAsyncSerch)
        self.pauseButton.clicked.connect(self.pauseAsyncSerch)
        self._model = QtGui.QStandardItemModel()
        self.tableInit()

        self._start_ip = '127.0.0.1'
        self._end_ip = '127.0.0.1'
        self._specificPort = 25565
        self._serverStatus = ServerStatus()
        self._totalLines = 0


    def tableInit(self):
        headersLabels = ["ID", "Server address", "Server description",
                         "Version", "Online", "Max players", "Country", "City",
                         "Hostname", "Ping"]

        self._model.setHorizontalHeaderLabels(headersLabels)
        self.tableView.setModel(self._model)

    def getWhoIsData(self, host):
        url = ''

    def aboutMessage(self):
        QtWidgets.QMessageBox.about(self, "About",
                                    "The program was created by rialbat\nVersion: 0.1\nMIT License")

    def startAsyncSerch(self):
        self.stopButton.setEnabled(True)
        self.pauseButton.setEnabled(True)
        self.pauseButton.setText("Pause")

        self._serverStatus._port = self.portSpinBox.value()

        self._start_ip = ipaddress.IPv4Address(self.startIpLineEdit.text())
        self._end_ip = ipaddress.IPv4Address(self.endIpLineEdit.text())

        for ip_int in range(int(self._start_ip), int(self._end_ip)+1):
            self._serverStatus._host = str(ipaddress.IPv4Address(ip_int))
            self._totalLines = self._totalLines + 1
            # ID
            itemID = QtGui.QStandardItem(str(self._totalLines))
            itemID.setTextAlignment(QtCore.Qt.AlignCenter) # type: ignore
            self._model.setItem(self._totalLines - 1, 0, itemID)
            # Server address
            itemSAdd = QtGui.QStandardItem(str(ipaddress.IPv4Address(ip_int)) + ":"
                                           + str(self.portSpinBox.value()))
            itemSAdd.setTextAlignment(QtCore.Qt.AlignCenter)  # type: ignore
            self._model.setItem(self._totalLines - 1, 1, itemSAdd)
            # Server description

            # Version

            # Online

            # Max players

            # Country, City, Hostname

            print(self._serverStatus.get_status())



    def stopAsyncSerch(self):
        #TODO stop actions
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
