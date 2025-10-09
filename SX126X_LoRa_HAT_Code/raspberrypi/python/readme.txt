Disclaimer: This repository was set up as a reswartch procject to support the lecture AEs from daniel wiebe und herbert palm in WS25. 
Die Bibliotehk soll als Grundlage für das dort durchgeführte Projekt dienen, in welchem die Studenten in der Vorlesung erlernte Grundlagen des Systems Enginieering anwenden und erste Erfahrungen 
in der Microcontrollerprogrammierung und Python sammeln. Auf Grund der ... wurde sich für den Raspberry Pi entschieden.

Lora 

- am meisten verwendet für Low power wide area networks 
- In Europa unlizensierten Frequenzband 868MHz 
- 863-870 MHz (ISM/SRD-Band) ist ohne individuelle Funklizenz freigeben
- leitungsloses Übertragungsverfahren auf der Bitübertragungsschicht (physical layer) [Wikipedia]
- klare Regelung wie viel Daten pro Sekunde gesendet werden dürfen -> Verstoß kann zu Problemen führen
- Nutzung ist genau durch die ETSI-Norm EN 300 220 und die Frequenznutzungsbestimmungen der Bundesnetzagentur (BNetzA) geregelt.
- Das Band darf maximal mit einem 1% Duty- Cycle genutze werden. Das heißt 36s pro Stunde (... Die Bibliothek garantiert die Einhaltung)



- bit rate vergleich mit Internet
- reichweite vergleich mit Internet

Vor und Nachteiel 

LoRaWAN ist die medium access control layer (MAC)
-Sterntopologie

Wieso LORA und nicht LoraWAN
Unterschied LORA und LoraWAN...
Der RaspberryPi ist nicht echtzeitkompatibel(?), LoraWAN benötigt allerdings eine Echtzeitkompatibilität, weswegen sich hier auf LORA beschränkt wird.



2. Einleitung: Was ist LORA und LoraWAN, vornachteiel zu wlan, wieso verwenden wir LORA und nicht LoraWAN
Quelle: [Wikipedia -> mit Link]

1.Head jumper umstecken (Bilder)

install code per pip

example code