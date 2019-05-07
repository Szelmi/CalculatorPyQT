#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication
from src.calculator import CalculatorWindow

app = QApplication(sys.argv)

calculator = CalculatorWindow()

sys.exit(app.exec_())


