from sx126x import sx126x
import time

if __name__ == "__main__":
    counter = 0
    schatz = {
        1: ("Schatz 1: liegt in Raum XYZ bei dem Pult. Du kannst es abholen und 62234 nach dem Code fragen.", 64535, 862),
        2: ("Schatz 2: liegt in Raum XYZ bei dem Pult. Du kannst es abholen und 62234 nach dem Code fragen.", 64535, 862),
        3: ("Schatz 3: liegt in Raum XYZ bei dem Pult. Du kannst es abholen und 62234 nach dem Code fragen.", 64535, 862),
        4: ("Schatz 4: liegt in Raum XYZ bei dem Pult. Du kannst es abholen und 62234 nach dem Code fragen.", 64535, 862),
        5: ("Schatz 5: liegt in Raum XYZ bei dem Pult. Du kannst es abholen und 62234 nach dem Code fragen.", 64535, 862)
    }

    node = sx126x(serial_num = "/dev/ttyS0",freq=868,addr=63535,power=22,rssi=True,air_speed=2400, relay=False, duty_cycle=0.01, buffer_size = 32)
    
    while True:
        for nr, (text, addr, freq) in schatz.items():
            node.send_string(addr, freq, text)
            print("Send: ", addr, freq)
            time.sleep(1)

        print("Counter: ", counter)
        time.sleep(5)
        counter += 1  