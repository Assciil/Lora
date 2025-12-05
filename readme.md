**Disclaimer:** 
Dieses Repository wurde im Rahmen eines universitären Forschungsprojekts zur Unterstützung der Lehrveranstaltung „Analyse und Entwurf von Systemen“ von **Daniel Wiebe** und **Herbert Palm** im **Wintersemester 2025/2026** entwickelt. Es basiert auf dem von *Waveshare* veröffentlichten Code [4] und dient als Grundlage für ein begleitendes Praxisprojekt, in dem Studierende die in der Vorlesung vermittelten Konzepte des Systems Engineering umsetzen und praktische Erfahrungen in der Mikrocontroller- und Python-Programmierung sammeln.

### 1. Einleitung  
Long Range (LoRa) ist eine Modulationsart, mit der kleine Datenmengen, beispielsweise Sensormesswerte, energieeffizient und leitungsfrei über mehrere Kilometer hinweg (Waveshare HAT 5km, sonnige Tag, open area [3]) übertragen werden können. Sie basiert auf einer Chirp-Spread-Spectrum-Modulation (CSS), die eine hohe Robustheit gegenüber Störungen bietet.

Häufig wird LoRa im Zusammenhang mit LoRaWAN genannt. Dabei handelt es sich um ein auf LoRa basierendes Kommunikationsprotokoll mit dem Low-Power Wide Area Networks (LPWANs) aufgebaut werden können. Das Protokoll von LoRaWAN setzt ein echtzeitfähige Hardware voraus, weswegen es ohne weiteren Zusatz nicht Raspberry Pi geeignet ist.[2]  

In Europa erfolgt der Betrieb im unlizenzierten ISM/SRD-Band 863–870 MHz, das ohne individuelle Funklizenz genutzt werden darf. Die Nutzung dieses Frequenzbands ist klar geregelt: maßgeblich sind die ETSI-Norm EN 300 220 sowie die Frequenznutzungsbestimmungen der Bundesnetzagentur (BNetzA). Eine zentrale Vorgabe ist der Duty-Cycle: Das Band darf in der Regel maximal zu 1 % belegt werden, d. h. 36 Sekunden Sendezeit pro Stunde pro Kanal. Außerdem beträgt die maximal erlaubte Sendeleistung 25 mW ERP. 

### 2. Hardwareaufbau - LoRa Kommunikation zwischen zwei Raspberry Pis  
Für die Punkt-zu-Punkt-Kommunikation werden zwei Raspberry Pis identisch konfiguriert. Auf beide wird je ein "SX1262 868M LoRa HAT" -Modul aufgesteckt. Auf jedem Modul wird eine Antenne aufgeschraubt und die Jumper werden gemäß untenstehendem Bild gesetzt.

Die Jumper sind bei beiden gemäß folgender Grafik zusetzen: 
![alt text](Jumper%20Config.png)

### 3. Installation  

### 3.1 Enable serial Port
Der Raspberry Pi kommuniziert über UART (seriell) mit dem Lora-Modul.

```bash
sudo raspi-config
```
Choose Interfacing Options -> Serial -> `No` -> `Yes`.
  - Would you like a login shell to be accessible over serial? -> `No`
  - Would you like the serial port hardware to be enabled? -> `Yes`

### 3.2 Virtuelle Umgebung
Eine virtuelle Umgebung ist ein abgetrennter Python-Arbeitsbereich mit eigenen installierten Paketen, welche unabhängig vom System sind.

#### Virtuelle Umgebung bauen

```bash
sudo apt install -y python3 python3-venv python3-pip  
python3 -m venv .<venv name>  
```

#### Virtuelle Umgebung aktivieren 

```bash
source .<venv name>/bin/activate 
```
- Mit `deactivate`kann die virtuelle Umgebung wieder verlassen werden.

#### Pakete installieren  
Installiert die Library und alle sonstigen notwendigen Pakete.

```bash
pip install -U pip  
pip install pyserial RPi.GPIO  
pip install "git+https://github.com/Assciil/Lora.git@main"  
```

### 4. Klassenbeschreibung `sx126x`
Repräsentiert ein SX126x-LoRa-Modul am Raspberry Pi und kapselt die gesamte UART-/GPIO-Konfiguration sowie Senden/Empfangen.

#### Konstruktor

```python
sx126x(
    freq: int,
    addr: int,
    power: int,
    buffer_size: int = 240
)
```

**Beschreibung**

Initialisiert das LoRa-Modul, setzt die GPIO-Pins, öffnet die serielle Schnittstelle
und schreibt die aktuellen Einstellungen ins Modul.

**Parameter**

| Name         | Typ    | Standard      | Beschreibung                                           |
|-------------|--------|---------------|--------------------------------------------------------|
| `freq`      | int    | –             | Frequenz in MHz (z.B. 868 für 868 MHz).               |
| `addr`      | int    | –             | Geräte-/Node-Adresse (0–65535).                       |
| `power`     | int    | –             | Sendeleistung in dBm (10, 13, 17, 22).                |
| `buffer_size` | int  | `240`         | Paket-/Buffergröße in Byte (240, 128, 64, 32).


### 4.1 Methoden

#### `set(...)`

```python
set(
    freq: int,
    addr: int,
    power: int,
    buffer_size: int = 240
)
```

Setzt die Funkparameter zur Laufzeit neu (Frequenz, Adresse, Leistung, Datenrate, etc.)
und schreibt sie ins Modul.

#### `receive()`

```python
receive() -> Optional[str]
```

Liest eingehende Daten vom Modul, gibt den Payload (ohne Header) als UTF-8-String zurück.

- Gibt `None` zurück, wenn keine Daten verfügbar sind.

#### `send_string(addr: int, freq_mhz: int, string: str)`

```python
send_string(addr: int, freq_mhz: int, string: str) -> None
```

Sendet einen String an einen Ziel-Knoten. Baut das Datenpaket inklusive Adressen und Frequenz-Offset auf.

**Parameter**

- `addr`: Zieladresse des Empfängers.
- `freq_mhz`: Ziel-Frequenz in MHz (z.B. 868).
- `string`: Nutzlast als Python-String (`str`), wird in UTF-8 kodiert.


### 4. Beispiel Code

### 4.1 Transmitter

```python
from sx126x import sx126x
import time

if __name__ == "__main__":
    node = sx126x(freq=868,addr=64535,power=22, buffer_size = 32)
    while True:
        node.send_string(64535, 868, "Hello world!")
        print("Daten gesendet!")
        time.sleep(10)
        
```

### 4.2 Receiver  
```python
from sx126x import sx126x  

if __name__ == "__main__":  
    node = sx126x(freq=868,addr=64535,power=22, buffer_size = 32) 
    while True:  
        text = node.receive()  
        if text is not None:  
            print("Received:", text) 
```

[1] https://papers.academic-conferences.org/index.php/eccws/article/view/3575  
[2] https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10122600  
[3] https://www.waveshare.com/wiki/SX1262_868M_LoRa_HAT  
[4] https://files.waveshare.com/upload/1/18/SX126X_LoRa_HAT_CODE.zip


