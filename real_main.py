#!/usr/bin/python

import time
import atexit
import RPi.GPIO as GPIO
import Sensors 

GPIO.setmode(GPIO.BOARD) 		# Needed for reading from range sensors 
atexit.register(GPIO.cleanup) 


if __name__ == '__main__': 
	# INITIALIZE SENSORS 
	rngf_LT = Sensors.HCSR04(7,13)  	# -> rngf_FL 
	rngf_LM = Sensors.HCSR04(19,21) 	# -> rngf_FM 
	rngf_LB = Sensors.HCSR04(23,22) 	# -> rngf_FR 
	rngf_RT = Sensors.HCSR04(8,12)  	# -> rngf_ML 
	rngf_RM = Sensors.HCSR04(16,18) 	# -> rngf_MR 
	rngf_RB = Sensors.HCSR04(24,26) 	# -> rngf_RM
	time.sleep(1.0) 		# Time for all sensors pins to settle 

	
