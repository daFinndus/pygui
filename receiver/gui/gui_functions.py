import sys
import time

from PyQt5 import QtWidgets

# Importiere die generierte UI-Klasse
from gui import Ui_PyGUI


class Functions_PyGUI():
    def __init__(self):
        self.ui = Ui_PyGUI()
        self.ui.setupUi(Dialog)

        self.app_running = False  # Variable to check if our app is running
        self.temperature_unit = "Kelvin"  # Our default temperature unit

        self.ui.button_update.clicked.connect(self.update_value)
        self.ui.button_start.clicked.connect(self.start)
        self.ui.button_stop.clicked.connect(self.stop)

        self.ui.comboBox_temp_unit.activated.connect(self.update_unit)

    #  Function to get our unit from the combobox
    def update_unit(self):
        print("Updated Unit to " + str(self.ui.comboBox_temp_unit.currentText()))
        if self.ui.comboBox_temp_unit.currentText() == "Kelvin [ K ]":
            self.temperature_unit = "Kelvin"
        elif self.ui.comboBox_temp_unit.currentText() == "Celsius [ °C ]":
            self.temperature_unit = "Celsius"
        elif self.ui.comboBox_temp_unit.currentText() == "Fahrenheit [ °F ]":
            self.temperature_unit = "Fahrenheit"

    #  Function for updating our text box with a certain value
    def update_value(self, value):
        self.ui.temperature_ouput.setText(str(self.calculate_value(value)))

    #  Function to calculate our temperature with the correct unit
    def calculate_value(self, raw_value):
        if self.temperature_unit == "Kelvin":
            value = raw_value
        elif self.temperature_unit == "Celsius":
            value = raw_value - 273.15
        elif self.temperature_unit == "Fahrenheit":
            value = raw_value * 1.8 - 459.67

        print(value)
        return value

    #  Function to start measuring our temperature
    def start(self):
        print("Starting...")
        self.app_running = True

    #  Function to stop measuring our temperature
    def stop(self):
        print("Stopping...")
        self.app_running = False


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)  # Create an instance of our app
    Dialog = QtWidgets.QMainWindow()  # Create an instance of our window
    ui = Functions_PyGUI()  # Create an instance of our class
    Dialog.show()  # Show our window
    sys.exit(app.exec_())
