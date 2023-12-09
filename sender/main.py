from uart import MyUart
import threading

port = "/dev/ttyS0"  # This is the port our receiver is connected to

uart = MyUart(port)


def data_receiver(uart):
    while True:
        data = uart.read_data()  # Read data from the sender


def data_sender(uart):
    while True:
        uart.send_data()  # Read data from the sender


if __name__ == "__main__":
    thread_recv = threading.Thread(target=data_receiver, args=(uart,))
    thread_recv.start()
    thread_send = threading.Thread(target=data_sender, args=(uart,))
    thread_send.start()
