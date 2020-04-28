# RFID-File-Decryption-Encryption
Encrypt/Dycrypt your files with RFID card and AES password with Arduino and Python3.

# How does it work?
The program uses an arduino script (ReadHex.ino) to read the NUID of the RFID card, then when manually copying the NUID hex code to (readNUID.ino) arduino script it prints to serial True/False based on if the NUID in readNUID.ino is the same on the card you scanned, then the serial is red by the python script is is true it encrypts the secret.txt file using AES enryption.

# Hardware Requirments:
<li >[Arduino Uno:](https://www.google.com)</li>
<li>RFID CARD</li>
<li>RFID READER</li>
