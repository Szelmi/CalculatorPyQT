#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from ui_calculator import Ui_Calculator


class CalculatorWindow(QtWidgets.QMainWindow, Ui_Calculator):
    firstNum = None
    userIsTypingSecondNumber = False
    blad = False
    iloscLiczb = 0

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.pushButton_0.clicked.connect(self.digit_pressed)
        self.pushButton_1.clicked.connect(self.digit_pressed)
        self.pushButton_2.clicked.connect(self.digit_pressed)
        self.pushButton_3.clicked.connect(self.digit_pressed)
        self.pushButton_4.clicked.connect(self.digit_pressed)
        self.pushButton_5.clicked.connect(self.digit_pressed)
        self.pushButton_6.clicked.connect(self.digit_pressed)
        self.pushButton_7.clicked.connect(self.digit_pressed)
        self.pushButton_8.clicked.connect(self.digit_pressed)
        self.pushButton_9.clicked.connect(self.digit_pressed)

        self.pushButton_kropka.clicked.connect(self.decimal_pressed)
        self.pushButton_plusMinus.clicked.connect(self.unary_operation_pressed)
        self.pushButton_procent.clicked.connect(self.unary_operation_pressed)

        self.pushButton_dodac.clicked.connect(self.binary_operation_pressed)
        self.pushButton_odjac.clicked.connect(self.binary_operation_pressed)
        self.pushButton_podzielic.clicked.connect(self.binary_operation_pressed)
        self.pushButton_pomnozyc.clicked.connect(self.binary_operation_pressed)

        self.pushButton_rownaSie.clicked.connect(self.equals_pressed)

        self.pushButton_usun.clicked.connect(self.clear_pressed)

        self.pushButton_dodac.setCheckable(True)
        self.pushButton_odjac.setCheckable(True)
        self.pushButton_pomnozyc.setCheckable(True)
        self.pushButton_podzielic.setCheckable(True)

    def digit_pressed(self):
        self.iloscLiczb += 1
        if self.iloscLiczb < 13:
            if self.blad is True:
                self.clear_pressed()
            button = self.sender()

            if (self.pushButton_dodac.isChecked() or self.pushButton_odjac.isChecked() or
                    self.pushButton_pomnozyc.isChecked() or self.pushButton_podzielic.isChecked())\
                    and (not self.userIsTypingSecondNumber):
                newLabel = format(float(button.text()), '.15g')
                self.userIsTypingSecondNumber = True
            else:
                if('.' in self.label.text()) and (button.text() == '0'):
                    newLabel = format(self.label.text() + button.text(), '.15')
                else:
                    newLabel = format(float(self.label.text() + button.text()), '.15g')

            self.label.setText(newLabel)

    def decimal_pressed(self):
        self.iloscLiczb += 1

        if self.blad is True:
            self.clear_pressed()
        if '.' not in self.label.text():
            self.label.setText(self.label.text() + '.')

    def unary_operation_pressed(self):
        if self.iloscLiczb < 13:
            if self.blad is True:
                self.clear_pressed()
            button = self.sender()
            labelNumber = float(self.label.text())

            if button.text() == '+/-':
                labelNumber = labelNumber * (-1)
            else:
                labelNumber = labelNumber * 0.01

            newLabel = format(labelNumber, '.15g')
            self.label.setText(newLabel)

    def binary_operation_pressed(self):
        self.iloscLiczb = 0
        if self.blad is True:
            self.clear_pressed()
        button = self.sender()
        self.firstNum = float(self.label.text())
        button.setChecked(True)

    def equals_pressed(self):
        if self.blad is True:
            self.clear_pressed()
        secondNum = float(self.label.text())
        if self.pushButton_dodac.isChecked():
            labelNumber = self.firstNum + secondNum
            newLabel = format(labelNumber, '.8g')
            self.label.setText(newLabel)
            self.pushButton_dodac.setChecked(False)
        elif self.pushButton_odjac.isChecked():
            labelNumber = self.firstNum - secondNum
            newLabel = format(labelNumber, '.8g')
            self.label.setText(newLabel)
            self.pushButton_odjac.setChecked(False)
        elif self.pushButton_pomnozyc.isChecked():
            labelNumber = self.firstNum * secondNum
            newLabel = format(labelNumber, '.8g')
            self.label.setText(newLabel)
            self.pushButton_pomnozyc.setChecked(False)
        elif self.pushButton_podzielic.isChecked():
            if secondNum == 0:
                self.label.setText("Nie dziel przez 0")
                self.blad = True
            else:
                labelNumber = self.firstNum / secondNum
                newLabel = format(labelNumber, '.8g')
                self.label.setText(newLabel)
            self.pushButton_podzielic.setChecked(False)

        self.userIsTypingSecondNumber = False

    def clear_pressed(self):
        self.iloscLiczb = 0
        self.pushButton_dodac.setChecked(False)
        self.pushButton_odjac.setChecked(False)
        self.pushButton_pomnozyc.setChecked(False)
        self.pushButton_podzielic.setChecked(False)

        self.userIsTypingSecondNumber = False

        self.blad = False

        self.label.setText('0')


