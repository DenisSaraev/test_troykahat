import troykahat
from time import sleep

PIN_WP_REL = 7 

wp = troykahat.wiringpi_io()
wp.pinMode(PIN_WP_REL, wp.OUTPUT)


try:
    while True:
        wp.digitalWrite(PIN_WP_REL, False) #set True for enable
        sleep(2)
        wp.digitalWrite(PIN_WP_REL, True)
        sleep(2)
    

except KeyboardInterrupt:
    print('The program was stopped by keyboard.')
    wp.digitalWrite(PIN_WP_REL, False)



