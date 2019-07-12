import serial
import hashlib
import random
import string
import base64
import time

def sendData(serialPort):
    serialPort.open()
    print(serialPort.name)
    letters=string.printable
    word=''.join(random.choices(letters, k=6000))
    print(word)
    encodedString=str.encode(word)
    #print(encodedString)
    encodedString=base64.b64encode(encodedString)
    print(len(encodedString))
    print(encodedString)
    checkOurs=str.encode(gen_checksum(encodedString))
    print(checkOurs)
    serialPort.write(checkOurs)
    #serialPort.write(encodedString) #may be too fast for arduino with a high enough k
    for i in range(0, len(encodedString)):
        serialPort.write(encodedString[i:i+1])
        #time.sleep(0.00001)
    print("finished sending")
    serialPort.close()

def setupPort(baudrate, port):
    ser = serial.Serial()
    ser.baudrate = baudrate
    ser.port = port
    ser.timeuot=0
    return ser

def gen_checksum(data):
    return hashlib.md5(data).hexdigest()

ser1 = setupPort(38400, 'COM15')
sendData(ser1)
