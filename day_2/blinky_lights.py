from machine import Pin
import time

def blink_twice(led):
    led.value(1)
    time.sleep(0.25)
    led.value(0)
    time.sleep(0.25)
    led.value(1)
    time.sleep(0.25)
    led.value(0)
    time.sleep(0.25)
    led.value(1)
    time.sleep(0.25)
    led.value(0)

red = Pin(18, Pin.OUT)
green = Pin(19, Pin.OUT)
amber = Pin(20, Pin.OUT)

counter = 1

while counter < 11:
    print(f"counter is {counter}")
    
    red.value(1)
    green.value(0)
    amber.value(0)

    time.sleep(0.5)
    blink_twice(red)
    time.sleep(0.5)

    red.value(0)
    green.value(1)
    amber.value(0)
    
    time.sleep(0.5)
    blink_twice(green)
    time.sleep(0.5)
    
    red.value(0)
    green.value(0)
    amber.value(1)
    
    time.sleep(0.5)
    blink_twice(amber)
    time.sleep(0.5)
    
    red.value(0)
    green.value(0)
    amber.value(0)
    
    counter += 1




