# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowzRrFbd.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStatusBar, QTableView,
    QVBoxLayout, QWidget)

from custommenu import CustomMenu
import rc_icons

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(882, 463)
        icon = QIcon()
        icon.addFile(u":/images/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"*{\n"
"	background:rgb(255,255,255);\n"
"}\n"
"#startButton\n"
"{\n"
"	background:rgb(0,133,252);\n"
"	border-radius:8px;\n"
"	font-size:15px;\n"
"	font-family:Century Gothic, sans-serif;\n"
"	color:rgb(255,255,255);\n"
"}\n"
"#startButton:pressed\n"
"{\n"
"	background:rgb(0,122,228);\n"
"	border-radius:8px;\n"
"	font-size:15px;\n"
"	font-family:Century Gothic, sans-serif;\n"
"	color:rgb(255,255,255);\n"
"}\n"
"#startButton:disabled\n"
"{\n"
"	background:rgb(143,188,228);\n"
"	border-radius:8px;\n"
"	font-size:15px;\n"
"	font-family:Century Gothic, sans-serif;\n"
"	color:rgb(255,255,255);\n"
"}\n"
"#pauseButton\n"
"{\n"
"	background:rgb(0,133,252);\n"
"	border-radius:8px;\n"
"	font-size:15px;\n"
"	font-family:Century Gothic, sans-serif;\n"
"	color:rgb(255,255,255);\n"
"}\n"
"#pauseButton:pressed\n"
"{\n"
"	background:rgb(0,122,228);\n"
"	border-radius:8px;\n"
"	font-size:15px;\n"
"	font-family:Century Gothic, sans-serif;\n"
"	color:rgb(255,255,255);\n"
"}\n"
"#pauseButton:disabled\n"
"{\n"
"	background:rgb(143"
                        ",188,228);\n"
"	border-radius:8px;\n"
"	font-size:15px;\n"
"	font-family:Century Gothic, sans-serif;\n"
"	color:rgb(255,255,255);\n"
"}\n"
"#stopButton\n"
"{\n"
"	background:rgb(0,133,252);\n"
"	border-radius:8px;\n"
"	font-size:15px;\n"
"	font-family:Century Gothic, sans-serif;\n"
"	color:rgb(255,255,255);\n"
"}\n"
"#stopButton:pressed\n"
"{\n"
"	background:rgb(0,122,228);\n"
"	border-radius:8px;\n"
"	font-size:15px;\n"
"	font-family:Century Gothic, sans-serif;\n"
"	color:rgb(255,255,255);\n"
"}\n"
"#stopButton:disabled\n"
"{\n"
"	background:rgb(143,188,228);\n"
"	border-radius:8px;\n"
"	font-size:15px;\n"
"	font-family:Century Gothic, sans-serif;\n"
"	color:rgb(255,255,255);\n"
"}\n"
"QGroupBox\n"
"{\n"
"	font-family:Century Gothic, sans-serif;\n"
"}\n"
"QMenu::item:selected\n"
"{\n"
"	background-color:rgb(204,232,255);\n"
"	color:rgb(0,0,0);\n"
"}")
        self.actionSave_results = QAction(MainWindow)
        self.actionSave_results.setObjectName(u"actionSave_results")
        self.actionSave_results.setEnabled(False)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionOpen_file = QAction(MainWindow)
        self.actionOpen_file.setObjectName(u"actionOpen_file")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.horizontalHeader().setStretchLastSection(True)

        self.horizontalLayout_10.addWidget(self.tableView)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QSize(264, 170))
        self.groupBox_2.setMaximumSize(QSize(264, 170))
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.startIpLabel = QLabel(self.groupBox_2)
        self.startIpLabel.setObjectName(u"startIpLabel")

        self.horizontalLayout_2.addWidget(self.startIpLabel)

        self.startIpLineEdit = QLineEdit(self.groupBox_2)
        self.startIpLineEdit.setObjectName(u"startIpLineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.startIpLineEdit.sizePolicy().hasHeightForWidth())
        self.startIpLineEdit.setSizePolicy(sizePolicy1)
        self.startIpLineEdit.setMinimumSize(QSize(129, 20))
        self.startIpLineEdit.setMaximumSize(QSize(129, 20))

        self.horizontalLayout_2.addWidget(self.startIpLineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.endIpLabel = QLabel(self.groupBox_2)
        self.endIpLabel.setObjectName(u"endIpLabel")

        self.horizontalLayout_3.addWidget(self.endIpLabel)

        self.endIpLineEdit = QLineEdit(self.groupBox_2)
        self.endIpLineEdit.setObjectName(u"endIpLineEdit")
        sizePolicy1.setHeightForWidth(self.endIpLineEdit.sizePolicy().hasHeightForWidth())
        self.endIpLineEdit.setSizePolicy(sizePolicy1)
        self.endIpLineEdit.setMinimumSize(QSize(129, 20))
        self.endIpLineEdit.setMaximumSize(QSize(129, 20))

        self.horizontalLayout_3.addWidget(self.endIpLineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.portLabel = QLabel(self.groupBox_2)
        self.portLabel.setObjectName(u"portLabel")

        self.horizontalLayout_4.addWidget(self.portLabel)

        self.portSpinBox = QSpinBox(self.groupBox_2)
        self.portSpinBox.setObjectName(u"portSpinBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.portSpinBox.sizePolicy().hasHeightForWidth())
        self.portSpinBox.setSizePolicy(sizePolicy2)
        self.portSpinBox.setMinimumSize(QSize(129, 20))
        self.portSpinBox.setMaximumSize(QSize(129, 20))
        self.portSpinBox.setMinimum(0)
        self.portSpinBox.setMaximum(100000)
        self.portSpinBox.setValue(25565)

        self.horizontalLayout_4.addWidget(self.portSpinBox)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.threadsLabel = QLabel(self.groupBox_2)
        self.threadsLabel.setObjectName(u"threadsLabel")

        self.horizontalLayout_5.addWidget(self.threadsLabel)

        self.threadsSpinBox = QSpinBox(self.groupBox_2)
        self.threadsSpinBox.setObjectName(u"threadsSpinBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.threadsSpinBox.sizePolicy().hasHeightForWidth())
        self.threadsSpinBox.setSizePolicy(sizePolicy3)
        self.threadsSpinBox.setMinimumSize(QSize(129, 20))
        self.threadsSpinBox.setMaximumSize(QSize(129, 20))
        self.threadsSpinBox.setMinimum(1)
        self.threadsSpinBox.setMaximum(200)

        self.horizontalLayout_5.addWidget(self.threadsSpinBox)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.timeOutLabel = QLabel(self.groupBox_2)
        self.timeOutLabel.setObjectName(u"timeOutLabel")

        self.horizontalLayout_6.addWidget(self.timeOutLabel)

        self.timeOutSpinBox = QSpinBox(self.groupBox_2)
        self.timeOutSpinBox.setObjectName(u"timeOutSpinBox")
        sizePolicy3.setHeightForWidth(self.timeOutSpinBox.sizePolicy().hasHeightForWidth())
        self.timeOutSpinBox.setSizePolicy(sizePolicy3)
        self.timeOutSpinBox.setMinimumSize(QSize(129, 20))
        self.timeOutSpinBox.setMaximumSize(QSize(129, 20))
        self.timeOutSpinBox.setMinimum(1)
        self.timeOutSpinBox.setMaximum(200)
        self.timeOutSpinBox.setValue(2)

        self.horizontalLayout_6.addWidget(self.timeOutSpinBox)


        self.verticalLayout.addLayout(self.horizontalLayout_6)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.IPsLabel = QLabel(self.groupBox)
        self.IPsLabel.setObjectName(u"IPsLabel")
        sizePolicy.setHeightForWidth(self.IPsLabel.sizePolicy().hasHeightForWidth())
        self.IPsLabel.setSizePolicy(sizePolicy)
        self.IPsLabel.setMinimumSize(QSize(75, 0))

        self.horizontalLayout_7.addWidget(self.IPsLabel)

        self.IPsLabelStat = QLabel(self.groupBox)
        self.IPsLabelStat.setObjectName(u"IPsLabelStat")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.IPsLabelStat.sizePolicy().hasHeightForWidth())
        self.IPsLabelStat.setSizePolicy(sizePolicy4)

        self.horizontalLayout_7.addWidget(self.IPsLabelStat)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.CheckedLabel = QLabel(self.groupBox)
        self.CheckedLabel.setObjectName(u"CheckedLabel")
        sizePolicy.setHeightForWidth(self.CheckedLabel.sizePolicy().hasHeightForWidth())
        self.CheckedLabel.setSizePolicy(sizePolicy)
        self.CheckedLabel.setMinimumSize(QSize(75, 0))

        self.horizontalLayout_8.addWidget(self.CheckedLabel)

        self.CheckedLabelStat = QLabel(self.groupBox)
        self.CheckedLabelStat.setObjectName(u"CheckedLabelStat")
        sizePolicy4.setHeightForWidth(self.CheckedLabelStat.sizePolicy().hasHeightForWidth())
        self.CheckedLabelStat.setSizePolicy(sizePolicy4)

        self.horizontalLayout_8.addWidget(self.CheckedLabelStat)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.FoundLabel = QLabel(self.groupBox)
        self.FoundLabel.setObjectName(u"FoundLabel")
        sizePolicy.setHeightForWidth(self.FoundLabel.sizePolicy().hasHeightForWidth())
        self.FoundLabel.setSizePolicy(sizePolicy)
        self.FoundLabel.setMinimumSize(QSize(75, 0))

        self.horizontalLayout_9.addWidget(self.FoundLabel)

        self.FoundLabelStat = QLabel(self.groupBox)
        self.FoundLabelStat.setObjectName(u"FoundLabelStat")
        sizePolicy4.setHeightForWidth(self.FoundLabelStat.sizePolicy().hasHeightForWidth())
        self.FoundLabelStat.setSizePolicy(sizePolicy4)

        self.horizontalLayout_9.addWidget(self.FoundLabelStat)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.startButton = QPushButton(self.centralwidget)
        self.startButton.setObjectName(u"startButton")
        sizePolicy.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy)
        self.startButton.setMinimumSize(QSize(83, 30))
        self.startButton.setMaximumSize(QSize(83, 30))

        self.horizontalLayout.addWidget(self.startButton)

        self.pauseButton = QPushButton(self.centralwidget)
        self.pauseButton.setObjectName(u"pauseButton")
        self.pauseButton.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pauseButton.sizePolicy().hasHeightForWidth())
        self.pauseButton.setSizePolicy(sizePolicy)
        self.pauseButton.setMinimumSize(QSize(83, 30))
        self.pauseButton.setMaximumSize(QSize(83, 30))

        self.horizontalLayout.addWidget(self.pauseButton)

        self.stopButton = QPushButton(self.centralwidget)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setEnabled(False)
        sizePolicy.setHeightForWidth(self.stopButton.sizePolicy().hasHeightForWidth())
        self.stopButton.setSizePolicy(sizePolicy)
        self.stopButton.setMinimumSize(QSize(83, 30))
        self.stopButton.setMaximumSize(QSize(83, 30))
        self.stopButton.setSizeIncrement(QSize(83, 30))

        self.horizontalLayout.addWidget(self.stopButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.horizontalLayout_10.addLayout(self.verticalLayout_3)


        self.gridLayout_3.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 882, 22))
        self.menuAbout = CustomMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuFile.addAction(self.actionSave_results)
        self.menuFile.addAction(self.actionOpen_file)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)

        self.retranslateUi(MainWindow)
        self.actionExit.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Minecraft server scanner", None))
        self.actionSave_results.setText(QCoreApplication.translate("MainWindow", u"Save results", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionOpen_file.setText(QCoreApplication.translate("MainWindow", u"Open file", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.startIpLabel.setText(QCoreApplication.translate("MainWindow", u"Starting IP address:", None))
        self.startIpLineEdit.setText("")
        self.endIpLabel.setText(QCoreApplication.translate("MainWindow", u"Ending IP address:", None))
        self.portLabel.setText(QCoreApplication.translate("MainWindow", u"Check specific port:", None))
        self.threadsLabel.setText(QCoreApplication.translate("MainWindow", u"Number of Threads:", None))
        self.timeOutLabel.setText(QCoreApplication.translate("MainWindow", u"Timeout:", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Statistics", None))
        self.IPsLabel.setText(QCoreApplication.translate("MainWindow", u"IPs:", None))
        self.IPsLabelStat.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.CheckedLabel.setText(QCoreApplication.translate("MainWindow", u"Checked:", None))
        self.CheckedLabelStat.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.FoundLabel.setText(QCoreApplication.translate("MainWindow", u"Servers found:", None))
        self.FoundLabelStat.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pauseButton.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.stopButton.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi
