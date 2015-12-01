#!/usr/bin/python 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 
# --> MOTORS.PY <-- 
# 
#  - This file does all setting up of the four DC motors that make up the 
#       drivetrain of the 2016 IEEE competition robot 
# 
# ***NOTE*** Before this code may be used on an RPi, some setup is needed: 
#       1) Enable I2C communication (see https://goo.gl/2XdkcB for steps)
#       2) Install Adafruit's Python library for the Motor HAT 
#               (see https://goo.gl/lvMvrf for steps) 
# 
#  Author: Ben Evans 
# 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

import Adafruit_MotorHAT 

mtrHAT = Adafruit_MotorHAT.Adafruit_MotorHAT( addr=0x60 ) 
# ^ creates object for talking with HAT over I2C 
lf_mtr_ch = 1                   # connect LF motor to MotorHAT Ch. 1 
rf_mtr_ch = 2                   # connect RF motor to MotorHAT Ch. 2 
lr_mtr_ch = 3                   # connect LR motor to MotorHAT Ch. 3 
rr_mtr_ch = 4                   # connect RR motor to MotorHAT Ch. 4 
LF_mtr = mtrHAT.getMotor( lf_mtr_ch )     # LF_mtr =  left front motor 
RF_mtr = mrtHAT.getMotor( rf_mtr_ch )     # RF_mtr = right front motor 
LR_mtr = mtrHAT.getMotor( lr_mtr_ch )     # LR_mtr =  left rear motor 
RR_mtr = mtrHAT.getMotor( rr_mtr_ch )     # RR_mtr = right rear motor 
# Set up a few aliases for entities from the Adafruit library 
FORWARD  = Adafruit_MotorHAT.Adafruit_MotorHAT.FORWARD
BACKWARD = Adafruit_MotorHAT.Adafruit_MotorHAT.BACKWARD


def releaseAllMotors(): 
	mHAT.getMotor(1).run( Adafruit_MotorHAT.Adafruit_MotorHAT.RELEASE ) 
	mHAT.getMotor(2).run( Adafruit_MotorHAT.Adafruit_MotorHAT.RELEASE ) 
	mHAT.getMotor(3).run( Adafruit_MotorHAT.Adafruit_MotorHAT.RELEASE ) 
	mHAT.getMotor(4).run( Adafruit_MotorHAT.Adafruit_MotorHAT.RELEASE ) 

def goFrwrd(speed): 			### MUST be passed a speed value 
	LR_mtr.run( FORWARD ) 		
	RR_mtr.run( FORWARD ) 		# Set motor directions 
	LF_mtr.run( FORWARD ) 		# ..if not set already 
	RF_mtr.run( FORWARD ) 		 
	LR_mtr.setSpeed( speed ) 	
	RR_mtr.setSpeed( speed ) 	# Set motor speeds to specified value 
	LF_mtr.setSpeed( speed ) 	# Set all motor speeds to specified value 
	RF_mtr.setSpeed( speed ) 	 

def goBckwrd(speed): 
	LR_mtr.run( BACKWARD )           
	RR_mtr.run( BACKWARD )           # Set motor directions 
	LF_mtr.run( BACKWARD )           # ..if not set already 
	RF_mtr.run( BACKWARD )            
	LR_mtr.setSpeed( speed )        
	RR_mtr.setSpeed( speed )        # Set motor speeds to specified value 
	LF_mtr.setSpeed( speed )        # Set all motor speeds to specified value 
	RF_mtr.setSpeed( speed )         





