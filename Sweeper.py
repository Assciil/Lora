from datetime import datetime
from sx126x import sx126x
import time

F_MIN     = 862     # sinnvoll für SX126x im 868-MHz-Band
F_MAX     = 870     # Beispiel: 868–878 MHz
STEP_F    = 1       # 1 MHz Schritte
STEP_T    = 10.0    # alle 10 Sekunden

ADDR      = 64535
POWER     = 22
RSSI_ON   = True
AIR_SPEED = 2400
BUFFER_SZ = 64

if __name__ == "__main__":
    freq = F_MIN
    last_time = time.monotonic()
    print("Last_time: ", last_time)

    node = sx126x(
        serial_num="/dev/ttyS0",
        freq=F_MIN,
        addr=ADDR,
        power=POWER,
        rssi=RSSI_ON,
        air_speed=AIR_SPEED,
        relay=False,
        duty_cycle=0.01,
        buffer_size=BUFFER_SZ,
    )

    # läuft dauerhaft weiter, Frequenz wird nur bis F_MAX hochgerampt
    while freq <= F_MAX:
        now = time.monotonic()

        # alle 10 s um 1 MHz erhöhen, solange freq <= F_MAX
        if (now - last_time) >= STEP_T:
            last_time = now
            print(datetime.now(), "Tuning to frequency:", freq, "MHz")

            # HIER deine set()-Methode verwenden
            node.set(
                freq=freq,
                addr=ADDR,
                power=POWER,
                rssi=RSSI_ON,
                air_speed=AIR_SPEED,
                buffer_size=BUFFER_SZ
            )
            freq += STEP_F

        # kein delay im Hauptloop – du empfängst permanent
        text = node.receive()
        if text is not None:
            print("Received:", text)
