#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

BeepPin = 37

def SetupBuzzer():
	GPIO.setmode(GPIO.BOARD)        # Numbers pins by physical location
	GPIO.setup(BeepPin, GPIO.OUT)   # Set pin mode as output
	GPIO.output(BeepPin, GPIO.HIGH) # Set pin to high(+3.3V) to off the beep

def Beep():
    GPIO.output(BeepPin, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(BeepPin, GPIO.LOW)
    time.sleep(0.5)

def Destroy():
	GPIO.output(BeepPin, GPIO.HIGH)    # beep off
	GPIO.cleanup()                     # Release resource