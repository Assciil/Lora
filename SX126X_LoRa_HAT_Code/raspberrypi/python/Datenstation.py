#import sys
import sx126x
#import threading
#import time
#import select
#import termios
#import tty
#from threading import Timer
from datetime import datetime

def writeToFile(value, path="data.txt"):
    now = datetime.now()
    datum = now.strftime("%d.%m.%Y")
    uhrzeit = now.strftime("%H:%M:%S")
    zeile = f"datum: {datum} uhrzeit: {uhrzeit} wert: {value}"
    with open(path, "a", encoding="utf-8") as f:
        f.write(zeile + "\n")

if __name__ == "__main__":
    node = sx126x.sx126x(serial_num = "/dev/ttyS0",freq=868,addr=65535,power=22,rssi=True,air_speed=2400,relay=False)
    while True:
        text = node.receive()
        if text is not None:
            print("Received:", text)
            writeToFile(text)