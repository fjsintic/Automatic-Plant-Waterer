from  machine import Pin,ADC
#from picoBreadboard import BUTTON
import utime


soil_probe = ADC(Pin(27)) #CHANGE PIN NUMBER

relay = Pin(12,Pin.OUT)

#button = BUTTON(4)

##bt4 = button(1)




def relay_on():
    relay.value(1)
    print("we pumpin' water now")

def relay_off():
    relay.value(0)
    print("No more pump for u")


    



#FIND MAX AND MIN MOISTURE
max_moisture = 27200 #56700  #710 ##10646 11186 #The value the soil sensor reads in machine number. The sensor is bonkers and likes to drasticly change ADC values
min_moisture = 56700 #27200 #672 ##10117 10802


#code provided by JC for geting moisture percentage
def get_moisture_percentage(moisture_level):
    point_1_x = min_moisture
    point_2_x = max_moisture
    point_1_y = 0                                                          #The def function and loop iteration was code provided by JC williams
    point_2_y = 100
    m = ((point_2_y - point_1_y) / (point_2_x - point_1_x))
    return int((m*moisture_level) - (m*min_moisture) + point_1_y)


while True: #always happining
    moisture_level = soil_probe.read_u16()
    
    moisture_level_percentage = get_moisture_percentage(moisture_level)
    
    print(moisture_level) 
    
    print(moisture_level_percentage)
        
    if moisture_level_percentage < 50:
        relay_on()
    else:
        relay_off()

        
    utime.sleep(2)
    

        
    


    
    
    
    
    
    
