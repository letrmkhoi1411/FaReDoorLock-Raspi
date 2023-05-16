import RPi.GPIO as GPIO
import time
import signal
import atexit

def RunMotor():
    atexit.register(GPIO.cleanup)
    servopin = 7
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(servopin, GPIO.OUT, initial=False)
    p = GPIO.PWM(servopin,50)
    p.start(0)
    for i in range(0,181,10):
        p.ChangeDutyCycle(2.5 + 10 * i / 180)
        time.sleep(0.02)
        p.ChangeDutyCycle(0)
        time.sleep(0.2)
    time.sleep(3)
    for i in range(181,0,-10):
        p.ChangeDutyCycle(2.5 + 10 * i / 180)
        time.sleep(0.02)
        p.ChangeDutyCycle(0)
        time.sleep(0.2)