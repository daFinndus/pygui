import serial
import time


class MyUart:
    def __init__(self, port):
        self.ser = serial.Serial(port, baudrate=9600, timeout=1)  # Open our serial port

    def read_data(self):
        data = self.ser.readline().decode('utf-8').strip()
        return data


port = "COM3"

uart = MyUart(port)

while True:
    data = uart.read_data()  # Read data from the sender
    if data:
        print(data)
    time.sleep(0.1)  # Wait for 0.1 seconds before reading again
