from sx126x import sx126x
import time

if __name__ == "__main__":
    string = "Hallo Willi, wie geht's? Lange schon nichts mehr von dir gehört. Ich hoffe, alles ist in Ordnung bei dir. Melde dich mal wieder. Liebe Grüße! From Lisa."
    node = sx126x(serial_num = "/dev/ttyS0",freq=868,addr=63535,power=13,rssi=True,air_speed=2400, relay=False, duty_cycle=0.01, buffer_size = 240)
    while True:
        node.send_string(64535, 868, string)  
        time.sleep(2)  