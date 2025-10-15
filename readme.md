Disclaimer: Dieses Repository wurde als Forschungsprojekt eingerichtet, um die Lehrveranstaltung „AEs“ von Daniel Wiebe und Herbert Palm im WS25 zu unterstützen.

Die Bibliothek dient als Grundlage für das begleitende Projekt, in dem Studierende die in der Vorlesung vermittelten Prinzipien des Systems Engineering anwenden und erste praktische Erfahrungen in der Mikrocontroller-Programmierung sowie in Python sammeln.


1. Einleitung
Dieses Projekt nutzt LoRa als Funkübertragungstechnik für ein energieeffizientes Sensornetz. 
LoRa ist eine der am häufigsten verwendeten Technologien für Low-Power-Wide-Area-Networks (LPWANs) und eignet sich ideal, um kleine Datenmengen über große Distanzen mit sehr geringem Stromverbrauch zu übertragen. LoRa ist eine Funkmodulation auf der physikalischen Schicht (Physical Layer) des OSI-Modells.

In Europa erfolgt der Betrieb im unlizenzierten 868-MHz-Bereich, genauer im ISM/SRD-Band 863–870 MHz, das ohne 
individuelle Funklizenz genutzt werden darf. Die Nutzung dieses Frequenzbands ist klar geregelt: maßgeblich sind 
die ETSI-Norm EN 300 220 sowie die Frequenznutzungsbestimmungen der Bundesnetzagentur (BNetzA). 
Eine zentrale Vorgabe ist der Duty-Cycle: Das Band darf in der Regel maximal zu 1 % belegt werden, d. h. 36 Sekunden Sendezeit pro Stunde pro Kanal. Außerdem darf die Sendeleistung maximal 25 mW ERP betragen.
Die verwendete Bibliothek stellt die Einhaltung sicher. (nochmal überprüfen) Die Verantwortung für regelkonformen Betrieb liegt dennoch beim Anwender.

Der Begriff LoRaWAN fällt häufig im Zusammenhang mit LoRa. LoRaWAN ist ein Kommunikationsprotokoll (MAC-Schicht) 
und Rahmenwerk, das Sicherheit auf Netzwerk- und Anwendungsebene (jeweils auf AES-128 basierend), Geräteadressierung sowie Geräteverwaltung bereitstellt [1].

Warum hier LoRa und nicht LoRaWAN
Da ein Raspberry Pi ohne zusätzliche Echtzeit-Hardware nicht hard-echtzeitfähig ist und das LoRaWAN-Protokoll 
für seine Empfangsfenster strenge Timing-Anforderungen stellt, wird in diesem Projekt LoRa (PHY) ohne LoRaWAN eingesetzt.

2. Hardwareaufbau
Die Jumper sind gemäß Bild zusetzen 
![alt text](image.png)

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



[1] https://papers.academic-conferences.org/index.php/eccws/article/view/3575