Disclaimer: Dieses Repository wurde im Rahmen eines universitären Forschungsprojekts zur Unterstützung der Lehrveranstaltung „Analyse und Entwurf von Systemen“ von Daniel Wiebe und Herbert Palm im Wintersemester 2025/2026 entwickelt. Es basiert auf dem von Waveshare veröffentlichten Code [4] und dient als Grundlage für ein begleitendes Praxisprojekt, in dem Studierende die in der Vorlesung vermittelten Konzepte des Systems Engineering umsetzen und praktische Erfahrungen in der Mikrocontroller- und Python-Programmierung sammeln.

1. Einleitung  
Long Range (LoRa) ist eine Modulationsart, mit der kleine Datenmengen, beispielsweise Sensormesswerte, energieeffizient und leitungsfrei über mehrere Kilometer hinweg (Waveshare HAT 5km, sonnige Tag, open area [3]) übertragen werden können. Sie basiert auf einer Chirp-Spread-Spectrum-Modulation (CSS), die eine hohe Robustheit gegenüber Störungen bietet.

Häufig wird LoRa im Zusammenhang mit LoRaWAN genannt. Dabei handelt es sich um ein auf LoRa basierendes Kommunikationsprotokoll mit dem Low-Power Wide Area Networks (LPWANs) aufgebaut werden können. Das Protokoll von LoRaWAN setzt ein echtzeitfähige Hardware voraus, weswegen es nicht Raspberry Pi geeignet ist.[2]  

In Europa erfolgt der Betrieb im unlizenzierten ISM/SRD-Band 863–870 MHz, das ohne individuelle Funklizenz genutzt werden darf. Die Nutzung dieses Frequenzbands ist klar geregelt: maßgeblich sind die ETSI-Norm EN 300 220 sowie die Frequenznutzungsbestimmungen der muss d Bundesnetzagentur (BNetzA). Eine zentrale Vorgabe ist der Duty-Cycle: Das Band darf in der Regel maximal zu 1 % belegt werden, d. h. 36 Sekunden Sendezeit pro Stunde pro Kanal. Außerdem beträgt die maximal erlaubte Sendeleistung 25 mW ERP. Die beigefügte Bibliothek stellt die Einhaltung der Richtlinien in Deutschland sicher. (nochmal überprüfen!!), dennoch liegt die Verantwortung für einen Regelkonformen Betrieb beim Anwender. 

2. Hardwareaufbau - LoRa Kommunikation zwischen zwei Raspberry Pis  
Für die Punkt-zu-Punkt-Kommunikation werden zwei Raspberry Pis identisch konfiguriert. Auf beide wird je ein "SX1262 868M LoRa HAT" -Modul aufgesteckt. Auf jedem Modul wir eine Antenne aufgeschraubt und die Jumper gemäß untenstehendem Bild gesetzt.

Die Jumper sind bei beiden  
![alt text](Jumper%20Config.png)

3. Installation  

3.1 Virtuelleumgebung bauen und aktivieren  
sudo apt install -y python3 python3-venv python3-pip  
cd <Projektverzeichnis>  
python3 -m venv .<venv name>  
source .<venv name>/bin/activate  

3.2 Pakete installieren  
pip install -U pip  
pip install pyserial RPi.GPIO  
pip install "git+https://github.com/Assciil/Lora.git@main"  

4. Example Code  

4.1 Transmitter  
from sx126x import sx126x  
import time  

if __name__ == "__main__":  
    node = sx126x(serial_num = "/dev/ttyS0",freq=868,addr=63535,power=22,rssi=True,air_speed=2400, buffer_size=128, relay=False, duty_cycle=0.01)  
    while True:  
        node.send_float(64535, 868, 23.5)  
        time.sleep(10)  

4.2 Receiver  
from datetime import datetime  
from sx126x import sx126x  

if __name__ == "__main__":  
    node = sx126x(serial_num = "/dev/ttyS0",freq=868,addr=64535,power=22,rssi=True,air_speed=2400,relay=False, duty_cycle=0.01)  
    while True:  
        text = node.receive()  
        if text is not None:  
            print("Received:", text)  

[1] https://papers.academic-conferences.org/index.php/eccws/article/view/3575  
[2] https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10122600  
[3] https://www.waveshare.com/wiki/SX1262_868M_LoRa_HAT  
[4] https://files.waveshare.com/upload/1/18/SX126X_LoRa_HAT_CODE.zip

