import sys
import sx126x
import threading
import time
import select
import termios
import tty
from threading import Timer

import struct

def send_float(addr: int, freq_mhz: int, value: str):
    """
    Schickt einen Float-Wert als 4-Byte IEEE-754 (little-endian) an einen Ziel-Node.

    addr      : Zieladresse (0..65535)
    freq_mhz  : Frequenz in MHz (z.B. 868)
    value     : zu sendender Float-Wert
    """
    # Offset-Frequenz wie in deinem Original
    base = 850 if int(freq_mhz) > 850 else 410
    offset_frequence = int(freq_mhz) - base

    # Float in 4 Bytes wandeln (little-endian 32-bit)
    payload = struct.pack('<f', float(value))

    # Paket wie gehabt aufbauen: [dst_hi][dst_lo][dst_off][src_hi][src_lo][src_off][payload...]
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
    node = sx126x.sx126x(serial_num = "/dev/ttyS0",freq=868,addr=0,power=22,rssi=True,air_speed=2400,relay=False)
    while True:
        send_float(0, 868, 'Hello World')  # Beispielwert
        time.sleep(20)  # Warte 20 s bis zum nächsten Senden