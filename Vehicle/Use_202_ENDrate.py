from classMotor_200_OneFunc import *
from machine import Pin, PWM
import time

A = Servo(18,50)
B = Motor(33,25,50)

rate = 800


B.go(rate)
time.sleep(1)
A.right()
B.stop()
time.sleep(2)
B.go(rate)
time.sleep(2)
print("to 1")
B.back(rate)
time.sleep(2)
A.left()
B.stop()
time.sleep(2)
B.go(rate)
time.sleep(2)
print("to 2")
B.back(rate)
time.sleep(2)
B.stop()
A.zero()