from datetime import datetime
from sx126x import sx126x
import time

F_MIN     = 862     # sinnvoll für SX126x im 868-MHz-Band
F_MAX     = 870     # Beispiel: 868–878 MHz
STEP_F    = 1       # 1 MHz Schritte
STEP_T    = 7.0    # alle 10 Sekunden

ADDR      = [64534, 64535]
POWER     = 22
RSSI_ON   = True
AIR_SPEED = 2400
BUFFER_SZ = 64

if __name__ == "__main__":
    freq = F_MIN
    last_time = time.monotonic()

    node = sx126x(
        serial_num="/dev/ttyS0",
        freq=F_MIN,
        addr=ADDR[0],
        power=POWER,
        rssi=RSSI_ON,
        air_speed=AIR_SPEED,
        relay=False,
        duty_cycle=0.01,
        buffer_size=BUFFER_SZ,
    )
    for address in ADDR:
        node.set_address(address)
        freq = F_MIN
        node.set_frequency(freq)
        # läuft dauerhaft weiter, Frequenz wird nur bis F_MAX hochgerampt

        while freq <= F_MAX:
            now = time.monotonic()

            # alle 10 s um 1 MHz erhöhen, solange freq <= F_MAX
            if (now - last_time) >= STEP_T:
                last_time = now
                freq += STEP_F
                print(datetime.now(), "Tuning to frequency:", freq, "MHz")
                # HIER deine set()-Methode verwenden
                node.set_frequency(freq)


            # kein delay im Hauptloop – du empfängst permanent
            text = node.receive()
            if text is not None:
                print("Received:", text)

            
        
