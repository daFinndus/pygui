from uart import MyUart

self.rpi_port = "/dev/ttyS0"  # Our rpi3 UART port
self.usb_port = "/dev/ttyUSB0"  # Our USB UART port

my_uart = MyUart(self.rpi_port)  # Create our UART object

print("Starting...")
my_uart.test()  # Start our test
