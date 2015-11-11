#!/usr/bin/python
# 
# Example of controlling GPIO pins with Python
# 

import Adafruit_BBIO.GPIO as GPIO
GPIO.setup("P8_10", GPIO.OUT)
GPIO.output("P8_10", GPIO.HIGH)
GPIO.cleanup()

GPIO.setup("GPIO0_26", GPIO.OUT)
GPIO.setup("P8_14", GPIO.IN)
if GPIO.input("P8_14"):
    print("HIGH")
else:
    print("LOW")

GPIO.add_event_detect("P9_12", GPIO.FALLING)
#your amazing code here
#detect wherever:
if GPIO.event_detected("P9_12"):
    print "event detected!"

GPIO.cleanup()
