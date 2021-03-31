from machine import Pin
import time

red = Pin(13, Pin.OUT)
orange = Pin(14, Pin.OUT)
green = Pin(0, Pin.OUT)

red.off()
orange.off()
green.off()

for i in range(5):
    red.on()
    time.sleep(1)
    orange.on()
    time.sleep(1)
    red.off()
    orange.off()

    green.on()
    time.sleep(1)
    green.off()

    orange.on()
    time.sleep(1)
    orange.off()
