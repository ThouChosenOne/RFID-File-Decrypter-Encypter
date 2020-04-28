# RFID-File-Decryption-Encryption
Encrypt/Dycrypt your files with RFID card and AES password with Arduino and Python3.

# How does it work?
The program uses an arduino script (ReadHex.ino) to read the NUID of the RFID card, then when manually copying the NUID hex code to (readNUID.ino) arduino script it prints to serial True/False based on if the NUID in readNUID.ino is the same on the card you scanned, then the serial is red by the python script is is true it encrypts the secret.txt file using AES enryption.

# Hardware Requirments:
- [Arduino Uno](https://www.amazon.com/Arduino-A000066-ARDUINO-UNO-R3/dp/B008GRTSV6/ref=sr_1_1?dchild=1&keywords=arduino+uno&qid=1588071902&sr=8-1)
- [RFID Card & Receiver](https://www.amazon.com/DONGHENG-Mifare-Reader-Arduino-Raspberry/dp/B07MKR3827/ref=sr_1_2?dchild=1&keywords=arduino+rfid+card&qid=1588072324&sr=8-2)

# Arduino Connections:
![myImage](/Arduino-Files/circuit.png)

# How to install:
- ``` git clone https://github.com/JaniniRami07/RFID-File-Decrypter-Encypter ```
- ```cd RFID-File-Decrypter-Encypter```
- ```cd Arduino-Files```
- Open readHex.ino and upload it to the Arduino
- Open serial in arduino program and scan your RFID card.
- Copy the hex code: xx xx xx xx to readNUIDino file and replace it in line ``` byte knownTac[4] = {xx, xx, xx, xx};```
- Upload readNUID to Arduino uno (Close the serial if open).
- Make a secret.txt file and put in it what you want to encrypt.
- run ```python3  RFIDReader.py```

# Author:
pr0xy07@tutanota.com
