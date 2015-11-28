#!/usr/bin/python

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 
# --> SENSORS.PY <-- 
# 
#  - Upon import, this library will initialize objects for each sensor 
# 		used on the robot and define functions for utilizing them 
# 
#  *NOTE* 
#     Import this file at start of 'main.py' 
#  
#  Author:  Ben Evans 
# 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

import time
import RPi.GPIO as GPIO
import HCSR04 

# INITIALIZE SENSORS # 
rngf_LT = HCSR04.HCSR04(7,13)  	# -> rngf_FL 
rngf_LM = HCSR04.HCSR04(19,21) 	# -> rngf_FM 
rngf_LB = HCSR04.HCSR04(23,22) 	# -> rngf_FR 
rngf_RT = HCSR04.HCSR04(8,12)  	# -> rngf_ML 
rngf_RM = HCSR04.HCSR04(16,18) 	# -> rngf_MR 
rngf_RB = HCSR04.HCSR04(24,26) 	# -> rngf_RM
time.sleep(1.0) 		# Time for all sensors pins to settle 

def OffAxis(): 
	FL_dist = 0 
	FR_dist = 0 
	FM_dist = 0 
	for i in range(0,5): 
		FL_dist += rngf_FL.MeasureOnce() 
		FR_dist += rngf_FR.MeasureOnce() 
		FM_dist += rngf_FM.MeasureOnce() 
		time.sleep() 	# settle time for all echo pins 
	FL_dist /= 5 	# (cm) 
	FR_dist /= 5 	# (cm) 
	FM_dist /= 5 	# (cm) 
