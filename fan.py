import troykahat
from time import sleep

PIN_AP_BUZZER = 7
PIN_AP_BUZZERs = 3

#ap = troykahat.analog_io()
#ap.pinMode(PIN_AP_BUZZER, ap.OUTPUT)

wp = troykahat.wiringpi_io()
wp.pinMode(PIN_AP_BUZZER, wp.OUTPUT)

try:
    while True:
        wp.digitalWrite(PIN_AP_BUZZER, True) #Hight brightness in sensor = Low brightness in LED


except KeyboardInterrupt:
    print('The program was stopped by keyboard.')
finally:
    wp.digitalWrite(PIN_AP_BUZZER, False)
    wp.digitalWrite(PIN_AP_BUZZERs, False)
    print('LED disabled.') 
