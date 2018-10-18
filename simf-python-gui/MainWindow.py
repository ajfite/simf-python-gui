# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(723, 747)
        icon = QtGui.QIcon.fromTheme("h")
        MainWindow.setWindowIcon(icon)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.stopCapButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopCapButton.setObjectName("stopCapButton")
        self.gridLayout_2.addWidget(self.stopCapButton, 7, 0, 1, 1)
        self.startCapButton = QtWidgets.QPushButton(self.centralwidget)
        self.startCapButton.setObjectName("startCapButton")
        self.gridLayout_2.addWidget(self.startCapButton, 7, 1, 1, 1)
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setMinimumSize(QtCore.QSize(70, 30))
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout_2.addWidget(self.lcdNumber, 0, 3, 1, 1)
        self.consoleWidget = QtWidgets.QListWidget(self.centralwidget)
        self.consoleWidget.setObjectName("consoleWidget")
        self.gridLayout_2.addWidget(self.consoleWidget, 6, 0, 1, 4)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView_7 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_7.setObjectName("graphicsView_7")
        self.gridLayout.addWidget(self.graphicsView_7, 3, 2, 1, 1)
        self.graphicsView_5 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_5.setObjectName("graphicsView_5")
        self.gridLayout.addWidget(self.graphicsView_5, 1, 1, 1, 1)
        self.graphicsView_8 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_8.setObjectName("graphicsView_8")
        self.gridLayout.addWidget(self.graphicsView_8, 3, 1, 1, 1)
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.gridLayout.addWidget(self.graphicsView_4, 2, 1, 1, 1)
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.gridLayout.addWidget(self.graphicsView_2, 2, 0, 1, 1)
        self.graphicsView_6 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_6.setObjectName("graphicsView_6")
        self.gridLayout.addWidget(self.graphicsView_6, 1, 2, 1, 1)
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.gridLayout.addWidget(self.graphicsView_3, 3, 0, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 1, 0, 1, 1)
        self.graphicsView_9 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_9.setObjectName("graphicsView_9")
        self.gridLayout.addWidget(self.graphicsView_9, 2, 2, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 4, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 4)
        spacerItem = QtWidgets.QSpacerItem(29, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 723, 30))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCapture_Settings = QtWidgets.QAction(MainWindow)
        self.actionCapture_Settings.setObjectName("actionCapture_Settings")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSource_Code = QtWidgets.QAction(MainWindow)
        self.actionSource_Code.setObjectName("actionSource_Code")
        self.actionLicense = QtWidgets.QAction(MainWindow)
        self.actionLicense.setObjectName("actionLicense")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuAbout.addAction(self.actionCapture_Settings)
        self.menuAbout.addAction(self.actionExit)
        self.menuFile.addAction(self.actionSource_Code)
        self.menuFile.addAction(self.actionLicense)
        self.menuFile.addAction(self.actionAbout)
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Solar Irradiance Microforecasting Control Panel"))
        self.stopCapButton.setText(_translate("MainWindow", "Stop Capture"))
        self.startCapButton.setText(_translate("MainWindow", "Start Capture"))
        self.label.setText(_translate("MainWindow", "Solar Irradiance Microforecasting Control Panel"))
        self.menuAbout.setTitle(_translate("MainWindow", "Fi&le"))
        self.menuFile.setTitle(_translate("MainWindow", "Abo&ut"))
        self.actionCapture_Settings.setText(_translate("MainWindow", "&Capture Settings"))
        self.actionExit.setText(_translate("MainWindow", "&Exit"))
        self.actionSource_Code.setText(_translate("MainWindow", "&Source Code"))
        self.actionLicense.setText(_translate("MainWindow", "&License"))
        self.actionAbout.setText(_translate("MainWindow", "&About"))

