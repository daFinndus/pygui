class MyUart:
    def __init__(self, port):
        self.port = port
        self.ser = serial.Serial(self.port, 9600)  # Open our serial port with a baud rate of 9600

    # Function to read our port
    def read_line(self, port):
        s = ""  # Our string to return

        while True:
            ch = port.read()  # Read our port as byte

            s += ch  # Add that byte to our string

            if ch == "\r":  # If enter (\r) is pressed return our string
                return s

    # Function to write to our port
    def test(self):
        while True:
            time.sleep(1)
            print("Sending some data...")
            self.ser.write("Hello World!")  # Write our string to our serial port
            rcv = self.read_line(self.ser)  # Read a line from our serial port
            print("Received: ", rcv)
