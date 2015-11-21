#!/usr/bin/python

import time
import atexit
import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BOARD)


def measureDist():
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        while GPIO.input(ECHO) == 0:
                pulse_start = time.time()
        while GPIO.input(ECHO) == 1:
                pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)
        return distance


if __name__ == '__main__':
        setup()
        distance = 0
        while True:
                distSum = 0
                for i in range(0,TAKES):
                        distSum += measureDist()
                distance = distSum/TAKES
                print("Distance: " + str(distance) + " cm")
                time.sleep(0.15)
