#!/usr/bin/python

import time
import atexit
import RPi.GPIO as GPIO
import Sensors 
import Motors 

GPIO.setmode(GPIO.BOARD) 		# Needed for reading from range sensors 

def onExitHousekeeping(): 
	GPIO.cleanup() 
	Motors.releaseAllMotors() 
	
atexit.register(onExitHousekeeping) 


if __name__ == '__main__': 


