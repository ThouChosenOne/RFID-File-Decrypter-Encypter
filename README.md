# RFID-File-Decryption-Encryption
Encrypt/Dycrypt your files with RFID card and AES password with Arduino and Python3.

# How does it work?
The program uses an arduino script (ReadHex.ino) to read the NUID of the RFID card, then when manually copying the NUID hex code to (readNUID.ino) arduino script it prints to serial True/False based on if the NUID in readNUID.ino is the same on the card you scanned, then the serial is red by the python script is is true it encrypts the secret.txt file using AES enryption.

# Hardware Requirments:
- [Arduino Uno](https://www.amazon.com/Arduino-A000066-ARDUINO-UNO-R3/dp/B008GRTSV6/ref=sr_1_1?dchild=1&keywords=arduino+uno&qid=1588071902&sr=8-1)
- [RFID Card & Receiver](https://www.amazon.com/DONGHENG-Mifare-Reader-Arduino-Raspberry/dp/B07MKR3827/ref=sr_1_2?dchild=1&keywords=arduino+rfid+card&qid=1588072324&sr=8-2)

# Arduino Connections:
![myImage](/Arduino-Files/circuit.png)
