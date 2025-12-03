from sx126x import sx126x
import time

if __name__ == "__main__":
    counter = 0
    string = "Schatz 1: liegt in Raum XYZ bei dem Pult. Du kannst es abholen und 62234 nach dem Code fragen."
    node = sx126x(freq=868,addr=64535,power=22, buffer_size = 32)
    while True:
        node.send_string(64535, 868, string)
        print("Send: ", counter)
        time.sleep(5)
        counter += 1  
        
