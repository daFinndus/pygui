from gui import Ui_PyGUI
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Functions:
    def __init__(self):
        self.ui = Ui_PyGUI()
        self.ui.setupUi(Dialog)
        self.ui.button_update.clicked.connect(self.update_result)

    def update_result(self):
        temp_celsius = float(self.ui.sampling_time_input.text())
        temp_kelvin = temp_celsius + 273.13
        self.ui.temperature_ouput.setText(str(temp_kelvin) + " K")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    my_gui = Ui_Functions()
    Dialog.show()
    sys.exit(app.exec_())
