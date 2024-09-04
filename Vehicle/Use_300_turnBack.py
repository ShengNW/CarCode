from classMotor_201_HighScale import *
from machine import Pin, PWM
import time

A = Servo(18,50)
B = Motor(33,25,50)


rate = 1000

B.go(rate)
time.sleep(1)
A.turn(120)
#A.right()
B.go(rate)
time.sleep(9)
B.stop()
A.zero()