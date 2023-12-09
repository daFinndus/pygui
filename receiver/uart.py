import serial
import time


class MyUart:
    def __init__(self, port):
        self.ser = serial.Serial(port, baudrate=9600, timeout=1)  # Open our serial port

    def send_data(self, data):
        self.ser.write(f'{data}'.encode('utf-8'))

    def read_data(self):
        data = self.ser.readline().decode('utf-8').strip()
        return data
