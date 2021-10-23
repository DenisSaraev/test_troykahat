import troykahat
from time import sleep

PIN_AP_BUZZER = 7
PIN_AP_POTH = 2

ap = troykahat.analog_io()

ap.pinMode(PIN_AP_BUZZER, ap.OUTPUT)
ap.pinMode(PIN_AP_POTH, ap.INPUT)

try:
    while True:
        PothValue=ap.analogRead(PIN_AP_POTH)
        ap.analogWrite(PIN_AP_BUZZER, PothValue) #Hight brightness in sensor = Low brightness in LED
        print (PothValue)
        sleep(0.5)
except KeyboardInterrupt:
    print('The program was stopped by keyboard.')
finally:
    ap.digitalWrite(PIN_AP_BUZZER, False)
    print('LED disabled.') 