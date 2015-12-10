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
	# BEGIN MAIN PROGRAM 
	while(1): 
		# goFrwrd(arg) where arg = speed 
		#     0 <= speed <= 255 
		Motors.goFrwrd(100) 
		time.sleep(1) 
		Motors.goBckWrd(100) 
		time.sleep(1) 
