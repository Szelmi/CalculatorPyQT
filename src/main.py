from PyQt5.QtWidgets import  QApplication, QWidget
import sys
from PyQt5 import QtCore, QtGui
from calculator import Kalkulator

def main():
    app = QApplication(sys.argv)

    okno = Kalkulator()
    sys.exit(app.exec_())

main()