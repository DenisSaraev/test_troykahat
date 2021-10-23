import troykahat
from time import sleep     

PIN_WP_LED = 7  

wp = troykahat.wiringpi_io()
wp.pinMode(PIN_WP_LED, wp.OUTPUT)

try:
    while True:
        wp.digitalWrite(PIN_WP_LED, True)
        sleep(0.5)
        wp.digitalWrite(PIN_WP_LED, False)
        sleep(0.5)
except KeyboardInterrupt:
    print('The program was stopped by keyboard.')
finally:
    wp.digitalWrite(PIN_WP_LED, False)
    print('LED disabled.')
    