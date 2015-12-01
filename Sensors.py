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

# from time import sleep  		# Already imported in HCSR04.py, so use that 
# import RPi.GPIO as GPIO 		# Shouldn't be needed here 
import HCSR04 

# INITIALIZE SENSORS # 
rngf_FL = HCSR04.HCSR04(7,13)  	# -> rangefinder: front left 
rngf_FM = HCSR04.HCSR04(19,21) 	# -> rangefinder: front mid 
rngf_FR = HCSR04.HCSR04(23,22) 	# -> rangefinder: front right 
rngf_ML = HCSR04.HCSR04(8,12)  	# -> rangefinder:  mid  left 
rngf_MR = HCSR04.HCSR04(16,18) 	# -> rangefinder:  mid  right 
rngf_RM = HCSR04.HCSR04(24,26) 	# -> rangefinder:  rear mid 
HCSR04.sleep(0.5) 			# Extra time for all sensor pins to settle 


def OffAxisBy(repeats=5): 
	FL_dist = 0 
	FR_dist = 0 
	FM_dist = 0 
	for i in range(0,repeats): 
		FL_dist += rngf_FL.MeasureOnce() 
		FR_dist += rngf_FR.MeasureOnce() 
		FM_dist += rngf_FM.MeasureOnce() 
		HCSR04.sleep(rngf_FM.setl_len) 	# Give time for sensors to settle 
	FL_dist /= repeats 			# +15deg dist in cm 
	FR_dist /= repeats 			# -15deg dist in cm 
	FM_dist /= repeats 			#   0deg dist in cm 

