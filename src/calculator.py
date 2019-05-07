from calcUI import Ui_Calculator
from PyQt5 import QtWidgets

class Kalkulator(QtWidgets.QMainWindow, Ui_Calculator):
    def __init__(self):
        super().__init__()

        self.interfejs()
        self.pushButton_5.clicked.connect(self.digit_pressd)

    def digit_pressd(self):
        print("Siema")
    def interfejs(self):
        self.setupUi(self)
        self.show()
