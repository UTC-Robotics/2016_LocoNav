#!/usr/bin/python

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 
# --> HCSR04.PY <-- 
# 
#  This class is to be used for initializing each individual HCSR04 ultra-
#    sonic ranging module used on the 2016 IEEE Competition robot. 
#  When creating instances, 2 arguments must be passed: 
# 	1) Pi GPIO pin no. for HCSR04 Trig pin 
# 	2) Pi GPIO pin no. for HCSR04 Echo pin 
# 
#  *NOTE* 
#     Instances are to be created in the 'Sensors.py' file. 
#     Give 1-2 secs after any instance initialization for pins to settle! 
# 
#  Author:  Ben Evans 
# 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

import time
import RPi.GPIO as GPIO

class HCSR04: 

	num_meas_4avg = 30 		# Number of measurements to average 
	trig_len = 0.00001 		# Pulse length to trigger HCSR04 (sec) 

	def __init__(self,pin1,pin2):  
		self.trig_pin = pin1 
		self.echo_pin = pin2 
		GPIO.setup(self.echo_pin, GPIO.IN) 
		GPIO.setup(self.trig_pin, GPIO.OUT) 
		GPIO.output(self.trig_pin, False) 
		self.pulse_start = 0 
		self.pulse_end = 0 
		self.pulse_dur = 0 
		self.new_dist = 0 
		
	def MeasureOnce(self): 
		GPIO.output(self.trig_pin, True) 
		time.sleep(self.trig_len) 
		GPIO.output(self.trig_pin, False) 
		while(GPIO.input(self.echo_pin)==0): 
			self.pulse_start = time.time() 
		while(GPIO.input(self.echo_pin)==1): 
			self.pulse_end = time.time() 
		self.pulse_dur = self.pulse_end - self.pulse_start 
		self.new_dist = self.pulse_dur * 17150 
		self.new_dist = round(self.new_dist, 2) 
		return(self.new_dist) 
		
		