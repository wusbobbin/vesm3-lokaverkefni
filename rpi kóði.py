from Adafruit_IO import *
from gpiozero import Button
import serial
prevline = "start"
aio = Client('wusbobbin', 'aio_lrVC41unO72xL8a742xE3nvHddBd')       
aio.send('soilmoisture', prevline)
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.flush()
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            if line != prevline:
                aio.send("soilmoisture", line)
                prevline = line
            print(line)