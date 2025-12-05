from datetime import datetime
from sx126x import sx126x


if __name__ == "__main__":
    node = sx126x(freq=862,addr=62333,power=22, buffer_size = 32)
    while True:
        text = node.receive()
        if text is not None:
            print("Received:", text)