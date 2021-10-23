import troykahat
from time import sleep

PIN_AP_WATER_1 = 1
PIN_AP_WATER_2 = 2
PIN_AP_WATER_3 = 3
PIN_AP_WATER_4 = 4
PIN_AP_WATER_5 = 5
PIN_AP_WATER_6 = 6
PIN_WP_MOSF = 1  

wp = troykahat.wiringpi_io()
wp.pinMode(PIN_WP_MOSF, wp.OUTPUT)
ap = troykahat.analog_io()
ap.pinMode(PIN_AP_WATER_1, ap.INPUT)
ap.pinMode(PIN_AP_WATER_2, ap.INPUT)
ap.pinMode(PIN_AP_WATER_3, ap.INPUT)
ap.pinMode(PIN_AP_WATER_4, ap.INPUT)
ap.pinMode(PIN_AP_WATER_5, ap.INPUT)
ap.pinMode(PIN_AP_WATER_6, ap.INPUT)

wp.digitalWrite(PIN_WP_MOSF, True) #set True for enable

try:
    while True:
        WaterValue_1=ap.analogRead(PIN_AP_WATER_1)
        WaterValue_human_readable_1 = str(WaterValue_1*100)
        print (WaterValue_human_readable_1+' % 1')
        WaterValue_2=ap.analogRead(PIN_AP_WATER_2)
        WaterValue_human_readable_2 = str(WaterValue_2*100)
        print (WaterValue_human_readable_2+' % 2')
        WaterValue_3=ap.analogRead(PIN_AP_WATER_3)
        WaterValue_human_readable_3 = str(WaterValue_3*100)
        print (WaterValue_human_readable_3+' % 3')
        WaterValue_4=ap.analogRead(PIN_AP_WATER_4)
        WaterValue_human_readable_4 = str(WaterValue_4*100)
        print (WaterValue_human_readable_4+' % 4')
        WaterValue_5=ap.analogRead(PIN_AP_WATER_5)
        WaterValue_human_readable_5 = str(WaterValue_5*100)
        print (WaterValue_human_readable_5+' % 5')
        WaterValue_6=ap.analogRead(PIN_AP_WATER_6)
        WaterValue_human_readable_6 = str(WaterValue_6*100)
        print (WaterValue_human_readable_6+' % 6')
        sleep(0.5)
except KeyboardInterrupt:
    print('The program was stopped by keyboard.')
    wp.digitalWrite(PIN_WP_MOSF, False)
