#!/usr/bin/python 

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 
# --> MOTORS.PY <-- 
# 
#  - This file does all setting up of the four DC motors that make up the 
#       drivetrain of the 2016 IEEE competition robot 
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
LF_mtr = mHAT.getMotor( lf_mtr_ch )     # LF_mtr =  left front motor 
RF_mtr = mHAT.getMotor( rf_mtr_ch )     # RF_mtr = right front motor 
LR_mtr = mHAT.getMotor( lr_mtr_ch )     # LR_mtr =  left rear motor 
RR_mtr = mHAT.getMotor( rr_mtr_ch )     # RR_mtr = right rear motor 
# Set up a few aliases for entities from the Adafruit library 
FORWARD  = Adafruit_MotorHAT.Adafruit_MotorHAT.FORWARD
BACKWARD = Adafruit_MotorHAT.Adafruit_MotorHAT.BACKWARD

