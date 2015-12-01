#!/usr/bin/python

import time
import atexit
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD) 		# Needed for reading from range sensors 
atexit.register(GPIO.cleanup) 


if __name__ == '__main__': 
	import Sensors 


