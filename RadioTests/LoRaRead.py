import serial
import hashlib
import base64
import time

def readData(serialPort):
    #received=serialPort.read(1)
    checktheirs = serialPort.read(32)
    print("checktheirs: ")
    print(checktheirs)
    if (checktheirs):
        serialPort.timeout=20
        word = serialPort.read(8000)
        checkours = gen_checksum(word).encode('ascii')
        print("checkours: ")
        print(checkours)
        print("in: ")
        print(word)
        #decoded=base64.b64decode(word)
        #print(decoded)
        serialPort.timeout=10

def openPort(baudrate, port):
    ser = serial.Serial()
    ser.baudrate = baudrate
    ser.port = port
    ser.timeout=10
    ser.open()
    return ser

def gen_checksum(data):
    return hashlib.md5(data).hexdigest()

ser2 = openPort(38400, 'COM14')

try: 
    while 1:
        print("reading data...")
        readData(ser2)

except KeyboardInterrupt:
    print("KeyboardInterrupt caught")
