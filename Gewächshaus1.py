from sx126x import sx126x
import time

if __name__ == "__main__":
    string = "23.5"
    node = sx126x(serial_num = "/dev/ttyS0",freq=868,addr=63535,power=22,rssi=True,air_speed=2400, buffer_size=128, relay=False, duty_cycle=0.01)
    while True:
        node.send_string(64535, 868, string)  
        time.sleep(10)  