import time

import serial
from temperature_sensor.temp_sens import TempSensor


class MyUart:
    def __init__(self, port):
        self.ser = serial.Serial(port, baudrate=9600, timeout=1)  # Open our serial port
        self.temp_sensor = TempSensor(1, 64)

    def send_data(self):
        time.sleep(1)
        data = self.temp_sensor.measure_temp()
        self.ser.write(f'{data}'.encode('utf-8'))

        return data


port = "/dev/ttyS0"  # This is the port our receiver is connected to

uart = MyUart(port)

while True:
    data = uart.send_data()  # Send data to the receiver
    print(data)
