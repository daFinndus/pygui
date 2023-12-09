import sys
import threading
from PyQt5 import QtWidgets
from uart import MyUart
from ui.gui import Ui_PyGUI
from ui.gui_functions import Functions_PyGUI


# Function to receive data from the sender
def data_receiver(uart, gui):
    while True:
        data = uart.read_data()  # Read data from the sender
        data = str(data)[:6]  # Convert to string and then apply slicing

        if data:
            try:
                float_data = float(data)  # Attempt to convert the sliced string to float
                print(float_data)
                gui.update_temp_value(float_data)  # Update GUI with the new value
            except ValueError as e:
                print(f"Error converting data to float: {e}")
        else:
            print("Currenctly receiving no data from the sender!")


if __name__ == "__main__":
    port = "/dev/ttyAMA0"  # This is the port our sender is connected to

    uart = MyUart(port)

    app = QtWidgets.QApplication(sys.argv)  # Create an instance of our app
    Dialog = QtWidgets.QMainWindow()  # Create an instance of our window
    py_gui = Functions_PyGUI(Ui_PyGUI, Dialog, uart)  # Create an instance of our class

    thread_recv = threading.Thread(target=data_receiver, args=(uart, py_gui))
    thread_recv.start()

    Dialog.show()  # Show our window
    sys.exit(app.exec_())
