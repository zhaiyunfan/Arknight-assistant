# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 5, 1, 1)
        self.spinBoxMax = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBoxMax.setMaximum(130)
        self.spinBoxMax.setObjectName("spinBoxMax")
        self.gridLayout.addWidget(self.spinBoxMax, 1, 4, 1, 1)
        self.spinBoxHead = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBoxHead.setMaximum(128)
        self.spinBoxHead.setObjectName("spinBoxHead")
        self.gridLayout.addWidget(self.spinBoxHead, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 6, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)
        self.lcdNumberTimeMin = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumberTimeMin.setObjectName("lcdNumberTimeMin")
        self.gridLayout.addWidget(self.lcdNumberTimeMin, 2, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 3, 1, 1)
        self.lcdNumberTimeHour = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumberTimeHour.setObjectName("lcdNumberTimeHour")
        self.gridLayout.addWidget(self.lcdNumberTimeHour, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        self.lcdNumberHour = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumberHour.setProperty("intValue", 0)
        self.lcdNumberHour.setObjectName("lcdNumberHour")
        self.gridLayout.addWidget(self.lcdNumberHour, 0, 0, 1, 1)
        self.lcdNumberMin = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumberMin.setObjectName("lcdNumberMin")
        self.gridLayout.addWidget(self.lcdNumberMin, 0, 4, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 5, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "分将回满"))
        self.label_3.setText(_translate("MainWindow", "初始化理智"))
        self.label_2.setText(_translate("MainWindow", "分钟后理智将回满"))
        self.label_4.setText(_translate("MainWindow", "时"))
        self.label_6.setText(_translate("MainWindow", "最大理智"))
        self.label.setText(_translate("MainWindow", "小时"))
        self.pushButton.setText(_translate("MainWindow", "初始化"))

