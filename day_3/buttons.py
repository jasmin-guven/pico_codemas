from machine import Pin
import time


# set the pin as an input and use a pull down
button_1 = Pin(13, Pin.IN, Pin.PULL_DOWN)
button_2 = Pin(8, Pin.IN, Pin.PULL_DOWN)
button_3 = Pin(3, Pin.IN, Pin.PULL_DOWN)

red = Pin(18, Pin.OUT)
green = Pin(19, Pin.OUT)
amber = Pin(20, Pin.OUT)


while True: 

    time.sleep(0.5) 
            
    if button_1.value() == 1: #If button 1 is pressed
        
        print("Button 1 pressed")
        
        red.toggle() # Toggle Red LED on/off
        
    elif button_2.value() == 1: #If button 1 is pressed
        
        print("Button 2 pressed")
        
        green.toggle() # Toggle Red LED on/off
    
    elif button_3.value() == 1: #If button 1 is pressed
        
        print("Button 3 pressed")
        
        amber.toggle() # Toggle Red LED on/off