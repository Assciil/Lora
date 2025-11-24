from datetime import datetime
from sx126x import sx126x
import time

F_MIN     = 862      # MHz
F_MAX     = 870      # MHz
STEP_F    = 1        # 1 MHz Schritte
STEP_T    = 7.0      # alle 7 Sekunden

ADDR_LIST = [64534, 64535]
POWER     = 22
RSSI_ON   = True
AIR_SPEED = 2400
BUFFER_SZ = 64

if __name__ == "__main__":
    # Node einmal initialisieren, irgendeine Startadresse ist ok
    node = sx126x(
        serial_num="/dev/ttyS0",
        freq=F_MIN,
        addr=ADDR_LIST[0],
        power=POWER,
        rssi=RSSI_ON,
        air_speed=AIR_SPEED,
        relay=False,
        duty_cycle=0.01,
        buffer_size=BUFFER_SZ,
    )

    for address in ADDR_LIST:
        print(f"\n=== Starte Rampe für Adresse {address} ===")

        # Startwerte für diese Adresse
        freq = F_MIN
        last_time = time.monotonic()

        # Startfrequenz für diese Adresse setzen
        node.set(
            freq=freq,
            addr=address,
            power=POWER,
            rssi=RSSI_ON,
            air_speed=AIR_SPEED,
            buffer_size=BUFFER_SZ,
            relay=False,
        )
        print(time.now(), "Tuning to frequency:", freq, "MHz")

        # Rampe: alle STEP_T Sekunden +1 MHz, bis F_MAX erreicht
        while True:
            now = time.monotonic()

            # alle STEP_T Sekunden einen Schritt
            if (now - last_time) >= STEP_T:
                last_time = now

                # wenn wir schon bei F_MAX sind, fertig mit dieser Adresse
                if freq >= F_MAX:
                    break

                freq += STEP_F
                print(time.now(), "Tuning to frequency:", freq, "MHz")

                node.set(
                    freq=freq,
                    addr=address,
                    power=POWER,
                    rssi=RSSI_ON,
                    air_speed=AIR_SPEED,
                    buffer_size=BUFFER_SZ,
                    relay=False,
                )

            # kein delay im Loop – Empfang läuft kontinuierlich
            text = node.receive()
            if text is not None:
                print("Received:", text)
