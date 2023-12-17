import time
import threading

import serial
from temperature_sensor.temp_sens import TempSensor


class MyUart:
    def __init__(self, port):
        self.ser = serial.Serial(port, baudrate=9600, timeout=1)  # Open our serial port
        self.temp_sensor = TempSensor(1, 64)
        self.temp_bool = False  # Default sampling state

        self.thread_send = threading.Thread(target=self.send_data)

    def send_data(self):
        while self.temp_bool:
            data = self.temp_sensor.measure_temp()
            self.ser.write(f'{data}'.encode('utf-8'))

    def read_data(self):
        data_bytes = self.ser.readline()
        data_str = data_bytes.decode('utf-8').strip()

        if data_str.isdigit():
            try:
                self.temp_sensor.sampling_time = float(data_str)
                print(f"Setting sampling time to {(self.temp_sensor.sampling_time / 1000)} seconds!")
            except ValueError as e:
                print(f"Error converting data to float: {e}")
        elif data_str == "True" and not self.thread_send.is_alive():
            self.thread_send = threading.Thread(target=self.send_data)
            print("Starting thread!")
            self.temp_bool = True
            self.thread_send.start()
        elif data_str == "False" and self.thread_send.is_alive():
            print("Stopping thread...")
            print(f"This can take up to {(self.temp_sensor.sampling_time / 1000)} seconds!")
            self.temp_bool = False
            self.thread_send.join()
        else:
            pass

        return data_str
