from sx126x import sx126x
import time

if __name__ == "__main__":
    counter = 0
    schatz = {
        1: ("Schatz 1: liegt in Raum XYZ bei dem Pult. Sende den Geheimcode an 63535  - Eigene Adresse", 64535, 862),
        2: ("Schatz 2: liegt in Raum XYZ bei dem Pult. Sende den Geheimcode an 63535  - <Eigene Adresse>", 64535, 865),
        3: ("Schatz 3: liegt in Raum XYZ bei dem Pult. Sende den Geheimcode an 63535  - <Eigene Adresse>", 64535, 866),
        4: ("Schatz 4: liegt in Raum XYZ bei dem Pult. Sende den Geheimcode an 63535  - <Eigene Adresse>", 64535, 867),
        5: ("Schatz 5: liegt in Raum XYZ bei dem Pult. Sende den Geheimcode an 63535  - <Eigene Adresse>", 64534, 863),
        6: ("Schatz 6: liegt in Raum XYZ bei dem Pult. Sende den Geheimcode an 63535  - <Eigene Adresse>", 64534, 865),
        7: ("Schatz 7: liegt in Raum XYZ bei dem Pult. Sende den Geheimcode an 63535  - <Eigene Adresse>", 64534, 868),
        8: ("Schatz 8: liegt in Raum XYZ bei dem Pult. Sende den Geheimcode an 63535  - <Eigene Adresse>", 64534, 869)

    }

    node = sx126x(freq=868,addr=64535,power=22, buffer_size = 32)
    
    while True:
        for nr, (text, addr, freq) in schatz.items():
            node.send_string(addr, freq, text)
            print("Send: ", addr, freq)
            time.sleep(1.4)

        print("Counter: ", counter)
        counter += 1


