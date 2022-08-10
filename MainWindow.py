# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowfmAsOF.ui'
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
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")

        self.gridLayout_2.addWidget(self.tableView, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QSize(264, 143))
        self.groupBox_2.setMaximumSize(QSize(264, 143))
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


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

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


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 1, 1, 1)

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
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pauseButton.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.stopButton.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

