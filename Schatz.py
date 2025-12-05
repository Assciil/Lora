from sx126x import sx126x
import time

if __name__ == "__main__":
    counter = 0
    schatz = {
        1: ("Schatz 1 Hinweis: Labor Systems Engineering E103 Tisch 2" , 64534, 862),
        2: ("Schatz 2 Hinweis: Liegt im Museum auf der mittleren Vitrine - Wandseite", 64534, 865),
        3: ("Schatz 3 Hinweis: Liegt im Lesesaal E0132 auf dem Tisch", 64534, 866),
        4: ("Schatz 4 Hinweis: Liegt im Systems Engineering E103 Tisch 1", 64534, 867),
        5: ("Schatz 5 Hinweis: Liegt im HM-Kino Tisch 1", 64535, 863),
        6: ("Schatz 6 Hiweis: Liegt im HM-Kino Tisch 2", 64535, 865),
        7: ("Schatz 7 Hiweis: Liegt im HM-Kino Tisch 3", 64535, 868),
        8: ("Schatz 8 Hinweis: Liegt im Lesesaal Tisch 2", 64535, 869)

    }

    node = sx126x(freq=868,addr=64535,power=22, buffer_size = 240)
    
    while True:
        for nr, (text, addr, freq) in schatz.items():
            node.send_string(addr, freq, text)
            print("Send: ", addr, freq)
            time.sleep(1.3)

        print("Counter: ", counter)
        counter += 1


