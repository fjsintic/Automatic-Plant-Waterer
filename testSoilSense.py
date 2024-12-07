from  machine import Pin,ADC
import utime

while True:
    soil_probe = ADC(Pin(27)) #CHANGE PIN NUMBER

    moisture = soil_probe.read_u16()

    print(moisture)


    utime.sleep(1)
