from classMotor_200_OneFunc import *
from machine import Pin, PWM
import time

A = Servo(18,50)
B = Motor(33,25,50)

rate = 800

def turn_right():
    #B = Motor(33,25,50)
    B.go(rate)
    time.sleep(1)
    A.right()
    B.go(rate)
    time.sleep(6)
    B.stop()
    A.zero()
def back_right():
    B.back(rate)
    time.sleep(1)
    A.right()
    B.back(rate)
    time.sleep(6)
    B.stop()
    A.zero()
def turn_left():
    #B = Motor(33,25,50)
    B.go(rate)
    time.sleep(1)
    A.left()
    B.go(rate)
    time.sleep(5)
    B.stop()
    A.zero()
def back_left():
    B.back(1000)
    time.sleep(1)
    A.left()
    B.back(rate)
    time.sleep(7)
    B.stop()
    A.zero()
#turn_right()
B.go(1000)
time.sleep(2)

turn_left()
#B = Motor(33,25,5000)
B.go(1000)
time.sleep(7)
back_left()
#back_right()

