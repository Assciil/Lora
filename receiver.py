from datetime import datetime
from sx126x import sx126x


if __name__ == "__main__":
    node = sx126x(freq=868,addr=64535,power=22, buffer_size = 240)
    while True:
        text = node.receive()
        if text is not None:
            print("Received:", text)