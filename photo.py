import troykahat
from time import sleep

PIN_AP_PHOTO = 2

ap = troykahat.analog_io()
ap.pinMode(PIN_AP_PHOTO, ap.INPUT)

try:
    while True:
        PhotoValue=ap.analogRead(PIN_AP_PHOTO)
        PhotoValue_V=3.3*PhotoValue
        PhotoValue_mV=1000*PhotoValue_V
        print (PhotoValue_V)
        sleep(1.0)
except KeyboardInterrupt:
    print('The program was stopped by keyboard.')
  