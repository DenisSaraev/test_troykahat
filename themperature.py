import troykahat
from time import sleep

PIN_AP_TEMP = 3

ap = troykahat.analog_io()
ap.pinMode(PIN_AP_TEMP, ap.INPUT)

try:
    while True:
        TempValue=ap.analogRead(PIN_AP_TEMP)        
        TempValue_V=3.3*TempValue
        TempValue_mV=1000*TempValue_V
        TempValue_C = TempValue_V*100-50
        #print(str(TempValue_V)+' V')
        print(str(TempValue_C)+' C')
        sleep(1.0)
except KeyboardInterrupt:
    print('The program was stopped by keyboard.')
