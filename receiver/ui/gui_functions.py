class Functions_PyGUI:
    def __init__(self, PyGUI, Dialog, uart):
        self.ui = PyGUI()
        self.ui.setupUi(Dialog)

        self.app_running = False  # Variable to check if our app is running
        self.temperature_unit = "Kelvin"  # Our default temperature unit

        self.ui.button_update.clicked.connect(self.update)
        self.ui.button_start.clicked.connect(self.start)
        self.ui.button_stop.clicked.connect(self.stop)

        self.uart = uart

        self.ui.comboBox_temp_unit.activated.connect(self.update_temp_unit)

    #  Function to get our unit from the combobox
    def update_temp_unit(self):
        print("Updated Unit to " + str(self.ui.comboBox_temp_unit.currentText()))
        if self.ui.comboBox_temp_unit.currentText() == "Kelvin [ K ]":
            self.temperature_unit = "Kelvin"
        elif self.ui.comboBox_temp_unit.currentText() == "Celsius [ °C ]":
            self.temperature_unit = "Celsius"
        elif self.ui.comboBox_temp_unit.currentText() == "Fahrenheit [ °F ]":
            self.temperature_unit = "Fahrenheit"

    #  Function for updating our text box with a certain value
    def update_temp_value(self, value):
        if value:
            self.ui.temperature_ouput.setText(str(self.calculate_value(float(value))))
        else:
            print("Received empty data")

    #  Function to calculate our temperature with the correct unit
    def calculate_value(self, raw_value):
        if self.temperature_unit == "Celsius":
            value = raw_value - 273.15
        elif self.temperature_unit == "Fahrenheit":
            value = raw_value * 1.8 - 459.67
        else:
            value = raw_value

        value = round(value, 2)  # Round our value to 2 decimal places
        return value

    #  Function to start measuring our temperature
    def start(self):
        self.uart.send_data("True")

    #  Function to stop measuring our temperature
    def stop(self):
        self.uart.send_data("False")

    #  Function to update our sampling time
    def update(self):
        try:
            sampling_time = int(self.ui.sampling_time_input.text())
            if sampling_time >= 0:
                self.uart.send_data(str(sampling_time))
            else:
                print("Value is not valid: Please enter a positive number.")
        except ValueError:
            print("Value is not valid: Please enter a valid number.")
