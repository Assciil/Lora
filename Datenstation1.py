from datetime import datetime
from sx126x import sx126x

def writeToFile(value, path="data.txt"):
    now = datetime.now()
    datum = now.strftime("%d.%m.%Y")
    uhrzeit = now.strftime("%H:%M:%S")
    zeile = f"datum: {datum} uhrzeit: {uhrzeit} wert: {value}"
    with open(path, "a", encoding="utf-8") as f:
        f.write(zeile + "\n")

if __name__ == "__main__":
    node = sx126x(serial_num = "/dev/ttyS0",freq=868,addr=64535,power=13,rssi=True,air_speed=2400,relay=False, duty_cycle=0.01, buffer_size = 32)
    while True:
        text = node.receive()
        if text is not None:
            print("Received:", text)
            writeToFile(text)