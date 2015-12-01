#!/usr/bin/python

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 
# --> HCSR04.PY <-- 
# 
#  This class is to be used for initializing each individual HCSR04 ultra-
#    sonic ranging module used on the 2016 IEEE Competition robot. 
#  When creating objects, 2 arguments must be passed: 
# 	1) Pi GPIO pin no. for HCSR04 Trig 
# 	2) Pi GPIO pin no. for HCSR04 Echo 
# 
#  *NOTE* 
#     Instances are to be created in the 'Sensors.py' file. 
# 
#  Author:  Ben Evans 
# 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

from time import sleep 
import RPi.GPIO as GPIO

class HCSR04: 

	num_meas_highAcc = 30 	# Average this number of measurements for HIGH accuracy 
	num_meas_gudEngh = 5 	# Average this number for GOOD ENOUGH accuracy 
	trig_len = 0.00001 		# Pulse length to trigger HCSR04 (10 ns as per manual) 
	setl_len = 0.010 		# Time length to settle after a measurement (1 ms, arbitrary) 

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
		sleep(self.setl_len) 	# Give time to settle after init 
		
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
		#sleep(self.setl_len) 
		return(self.new_dist) 
		
		