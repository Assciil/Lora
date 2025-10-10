from sx126x import sx126x
import time

def send_float(addr: int, freq_mhz: int, value: float):
    base = 850 if int(freq_mhz) > 850 else 410
    offset_frequence = int(freq_mhz) - base

    # Float → String (z. B. 2 Nachkommastellen, Punkt als Dezimaltrenner)
    text = f"{value:.2f}"              # → "23.75"
    payload = text.encode("utf-8")     # String → Bytes

    data = bytes([
        (addr >> 8) & 0xFF,
        addr & 0xFF,
        offset_frequence & 0xFF,
        (node.addr >> 8) & 0xFF,
        node.addr & 0xFF,
        node.offset_freq & 0xFF,
    ]) + payload

    node.send(data)



if __name__ == "__main__":
    receive_adress = 65535  
    node = sx126x(serial_num = "/dev/ttyS0",freq=868,addr=65535,power=22,rssi=True,air_speed=2400, buffer_size=128, relay=False, duty_cycle=0.01)
    while True:
        send_float(64535, 868, 23.5)  
        time.sleep(20)  # Warte 20 s bis zum nächsten Senden