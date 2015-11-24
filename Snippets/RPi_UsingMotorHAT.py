#!/usr/bin/python 

# 
# RPi_UsingMotorHAT.py 
# -> simple functions and examples for interfacing with the 
#      Adafruit DC/Stepper Motor HAT for Raspberry Pi 
# 
# ***NOTE*** in order to use this code on a Pi, some setup is needed: 
# 	1) Enable I2C communication (see https://goo.gl/2XdkcB for steps)
# 	2) Install Adafruit's Python library for the Motor HAT 
# 		(see https://goo.gl/lvMvrf for steps) 
# 

import Adafruit_MotorHAT 
import time 
import atexit 

def setupMotorHAT(): 
	mHAT = Adafruit_MotorHAT.Adafruit_MotorHAT( addr=0x60 ) 
	# ^ creates object for talking with HAT over I2C 
	lf_mtr_ch = 1 			# connect LF motor to MotorHAT Ch. 1 
	rf_mtr_ch = 2 			# connect RF motor to MotorHAT Ch. 2 
	lr_mtr_ch = 3 			# connect LR motor to MotorHAT Ch. 3 
	rr_mtr_ch = 4 			# connect RR motor to MotorHAT Ch. 4 
	LF_mtr = mHAT.getMotor( lf_mtr_ch ) 	# LF_mtr =  left front motor 
	RF_mtr = mHAT.getMotor( rf_mtr_ch ) 	# RF_mtr = right front motor 
	LR_mtr = mHAT.getMotor( lr_mtr_ch ) 	# LR_mtr =  left rear motor 
	RR_mtr = mHAT.getMotor( rr_mtr_ch ) 	# RR_mtr = right rear motor 
	# Set up a few aliases for Adafruit library entities 
	FORWARD  = Adafruit_MotorHAT.Adafruit_MotorHAT.FORWARD 
	BACKWARD = Adafruit_MotorHAT.Adafruit_MotorHAT.BACKWARD

def releaseAllMotors():
	mHAT.getMotor(1).run( Adafruit_MotorHAT.Adafruit_MotorHAT.RELEASE ) 
	mHAT.getMotor(2).run( Adafruit_MotorHAT.Adafruit_MotorHAT.RELEASE ) 
	mHAT.getMotor(3).run( Adafruit_MotorHAT.Adafruit_MotorHAT.RELEASE ) 
	mHAT.getMotor(4).run( Adafruit_MotorHAT.Adafruit_MotorHAT.RELEASE ) 


if __name__ == "__main__": 
	setupMotorHAT() 
	atexit.register( releaseAllMotors ) 
	
	while( True ): 
		LR_mtr.run( FORWARD ) 		# Set motor direction 
		RR_mtr.run( FORWARD ) 		# ...for all 
		LF_mtr.run( FORWARD ) 
		RF_mtr.run( FORWARD ) 

		for i in range(255): 
			LR_mtr.setSpeed( i ) 	# Ramp speed up from off
			RR_mtr.setSpeed( i ) 	# ...to highest possible 
			LF_mtr.setSpeed( i ) 
			RF_mtr.setSpeed( i ) 
			time.sleep( 0.1 ) 

		for i in reversed(range(255)): 
			LR_mtr.setSpeed( i ) 	# Ramp speed back down 
			RR_mtr.setSpeed( i ) 	# ...to off 
			LF_mtr.setSpeed( i ) 
			RF_mtr.setSpeed( i ) 
			time.sleep( 0.1 ) 

		LR_mtr.run( BACKWARD ) 		# Now change direction 
		RR_mtr.run( BACKWARD ) 		# ...for all 
		LF_mtr.run( BACKWARD ) 
		RF_mtr.run( BACKWARD ) 

		for i in range(255): 
			LR_mtr.setSpeed( i ) 	# And repeat the cycle 
			RR_mtr.setSpeed( i ) 	# ...through all speeds 
			LF_mtr.setSpeed( i ) 
			RF_mtr.setSpeed( i ) 
			time.sleep( 0.1 ) 

		for i in reversed(range(255)): 
			LR_mtr.setSpeed( i ) 
			RR_mtr.setSpeed( i ) 
			LF_mtr.setSpeed( i ) 
			RF_mtr.setSpeed( i ) 
			time.sleep( 0.1 ) 
		
		time.sleep( 1 ) 
	# END LOOP 

