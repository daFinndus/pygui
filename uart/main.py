import serial
import time

port = "/dev/ttyS0"  # Our port name


# Method to read our port
def readline(port):
    s = ""  # Our string to return

    while True:
        ch = port.read()  # Read our port as byte
        ch = ch.decode("utf-8")  # Decode byte string to utf-8
        s += ch

        return s


ser = serial.Serial(port, 9600)  # Open our serial port with a baud rate of 9600

print("Starting...")
while True:
    time.sleep(1)
    print("Sending sync...")
    ser.write("A".encode("utf-8"))  # Write our string to our serial port
    rcv = readline(ser)  # Read a line from our serial port
    print("Received: ", rcv)
