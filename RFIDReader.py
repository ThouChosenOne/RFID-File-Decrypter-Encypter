import os
import sys
import time
import serial
import pyAesCrypt




bufferSize = 64 * 1024
file_to_encrypt = 'secret.txt'
file_to_decrypt = 'secret.txt.aes'

ser = serial.Serial(
port = "COM6",
baudrate = 9600,
bytesize = serial.EIGHTBITS,
parity = serial.PARITY_NONE,
stopbits = serial.STOPBITS_ONE,
timeout = 1,
xonxoff = False,
rtscts = False,
dsrdtr = False,
writeTimeout = 2
)


def encryptFile():
    with open(file_to_encrypt, "rb") as fIn:
        with open(file_to_decrypt, "wb") as fOut:
            pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)
            fOut.close()
        fIn.close()
    os.remove(file_to_encrypt)




def decrypt_file():
    encFileSize = os.stat(file_to_decrypt).st_size
    with open(file_to_decrypt, "rb") as fIn:
        try:
            with open(file_to_encrypt, "wb") as fOut:
                pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encFileSize)
                fOut.close()
            fIn.close()
        except ValueError:
            os.remove("dataout.txt")
    os.remove(file_to_decrypt)

loop = True
print('[+]RFID Scanner started, put the right card on the scanner...')
while loop:
    data = ser.readline()
    time.sleep(0.1)
    if 'True' in str(data):
        print('\n[+]Access Granted!')
        loop = False
    elif 'False' in str(data):
        print("[+]Access Failed!")


if loop == False:
    if os.path.isfile(file_to_decrypt):
        password = input('[+]Enter {} decryption password: '.format(file_to_decrypt))
        print('[+]Decrypting file...')
        decrypt_file()
    else:
        if os.path.isfile(file_to_encrypt):
            password = input('[+]Enter {} encryption password: '.format(file_to_encrypt))
            print('[+]Encrypting file...')
            encryptFile()
        else:
            print('[+] There is no {} file in the directory, please make one.'.format(file_to_encrypt))
            sys.exit()
