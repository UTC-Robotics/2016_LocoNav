#!/usr/bin/python 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 
# --> MAINFUNCS.PY <-- 
# 
#  This library contains supporting functions for the Nav system that make 
#   use of objects that must first be created in the main program. 
#   *THEREFORE* 
#      -> this library cannot be imported in 'main.py' until after 
#          all sensor and motor objects have been created.  
#  These functions placed here rather than 'main.py' simply for abstraction. 
# 
#  Author:  Ben Evans 
# 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

import time 
import RPi.GPIO as GPIO 
from numpy import sin, cos, tan, pi 

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
