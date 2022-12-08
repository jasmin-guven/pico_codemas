from machine import Pin
import time

onboard_led = Pin(25, Pin.OUT)

repeats = 10

for i in range(repeats):

    onboard_led.value(1)

    time.sleep(2)
    
    onboard_led.value(0)
    
    time.sleep(2)
    