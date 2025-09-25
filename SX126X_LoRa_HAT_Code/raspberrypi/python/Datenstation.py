import sys
import sx126x
import threading
import time
import select
import termios
import tty
from threading import Timer

if __name__ == "__main__":
    node = sx126x.sx126x(serial_num = "/dev/ttyS0",freq=868,addr=0,power=22,rssi=True,air_speed=2400,relay=False)
    while True:
        text = node.receive()
        if text is not None:
            print("Received:", text)