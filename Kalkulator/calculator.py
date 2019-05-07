# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(241, 361)
        MainWindow.setStyleSheet("QLabel {\n"
"  qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"background-color : white;")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setStyleSheet("  background-color: rgb(250, 128, 114);\n"
"")
        self.label.setObjectName("label")
        self.pushButton_usun = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_usun.setGeometry(QtCore.QRect(0, 60, 61, 61))
        self.pushButton_usun.setStyleSheet("QPushButton {\n"
"  background-color: rgb(30, 144, 255);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.pushButton_usun.setObjectName("pushButton_usun")
        self.pushButton_plusMinus = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_plusMinus.setGeometry(QtCore.QRect(60, 60, 61, 61))
        self.pushButton_plusMinus.setStyleSheet("QPushButton {\n"
"  background-color: rgb(30, 144, 255);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.pushButton_plusMinus.setObjectName("pushButton_plusMinus")
        self.pushButton_procent = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_procent.setGeometry(QtCore.QRect(120, 60, 61, 61))
        self.pushButton_procent.setStyleSheet("QPushButton {\n"
"  background-color: rgb(30, 144, 255);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.pushButton_procent.setObjectName("pushButton_procent")
        self.pushButton_podzielic = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_podzielic.setGeometry(QtCore.QRect(180, 60, 61, 61))
        self.pushButton_podzielic.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 0, 255);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_podzielic.setObjectName("pushButton_podzielic")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_9.setGeometry(QtCore.QRect(120, 120, 61, 61))
        self.pushButton_9.setStyleSheet("QPushButton {\n"
"   background-color: rgb(124, 252, 0);\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_pomnozyc = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_pomnozyc.setGeometry(QtCore.QRect(180, 120, 61, 61))
        self.pushButton_pomnozyc.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 20, 147);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_pomnozyc.setObjectName("pushButton_pomnozyc")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 120, 61, 61))
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"   background-color: rgb(124, 252, 0);\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_8.setGeometry(QtCore.QRect(60, 120, 61, 61))
        self.pushButton_8.setStyleSheet("QPushButton {\n"
"   background-color: rgb(255, 248, 220);\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_6.setGeometry(QtCore.QRect(120, 180, 61, 61))
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"   background-color: rgb(255, 248, 220);\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_dodac = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_dodac.setGeometry(QtCore.QRect(180, 180, 61, 61))
        self.pushButton_dodac.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 0, 255);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_dodac.setObjectName("pushButton_dodac")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 180, 61, 61))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"   background-color: rgb(255, 248, 220);\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_5.setGeometry(QtCore.QRect(60, 180, 61, 61))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"   background-color: rgb(124, 252, 0);\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 240, 61, 61))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"   background-color: rgb(124, 252, 0);\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_odjac = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_odjac.setGeometry(QtCore.QRect(180, 240, 61, 61))
        self.pushButton_odjac.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 20, 147);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_odjac.setObjectName("pushButton_odjac")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_1.setGeometry(QtCore.QRect(0, 240, 61, 61))
        self.pushButton_1.setStyleSheet("QPushButton {\n"
"   background-color: rgb(124, 252, 0);\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 240, 61, 61))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"   background-color: rgb(255, 248, 220);\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_kropka = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_kropka.setGeometry(QtCore.QRect(120, 300, 61, 61))
        self.pushButton_kropka.setStyleSheet("QPushButton {\n"
"  background-color: rgb(30, 144, 255);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #BEBEBE, stop: 1 #D7D7D7);\n"
"}")
        self.pushButton_kropka.setObjectName("pushButton_kropka")
        self.pushButton_rownaSie = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_rownaSie.setGeometry(QtCore.QRect(180, 300, 61, 61))
        self.pushButton_rownaSie.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 0, 255);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #FF7832, stop: 1 #FF9739);\n"
"}")
        self.pushButton_rownaSie.setObjectName("pushButton_rownaSie")
        self.pushButton_0 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_0.setGeometry(QtCore.QRect(0, 300, 121, 61))
        self.pushButton_0.setStyleSheet("QPushButton {\n"
"   background-color: rgb(240, 230, 140);\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"")
        self.pushButton_0.setObjectName("pushButton_0")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "0"))
        self.pushButton_usun.setText(_translate("MainWindow", "C"))
        self.pushButton_plusMinus.setText(_translate("MainWindow", "+/-"))
        self.pushButton_procent.setText(_translate("MainWindow", "%"))
        self.pushButton_podzielic.setText(_translate("MainWindow", "/"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_pomnozyc.setText(_translate("MainWindow", "x"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_dodac.setText(_translate("MainWindow", "+"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_odjac.setText(_translate("MainWindow", "-"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_kropka.setText(_translate("MainWindow", "."))
        self.pushButton_rownaSie.setText(_translate("MainWindow", "="))
        self.pushButton_0.setText(_translate("MainWindow", "0"))


