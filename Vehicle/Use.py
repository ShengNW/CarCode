from classMotor import *
from machine import Pin, PWM
import time
S1= Pin(33,Pin.IN)#PWM(Pin(25), freq=50, duty=0)
S1.value(1)


A = Servo(18,50)
time.sleep(2)
A.turn(20)
time.sleep(1)
A.turn(10)
B = Motor(33,50)
time.sleep(1)
B.go(128)
time.sleep(2)
B.stop()
C = Motor(25,50)
time.sleep(1)
C.go(128)
time.sleep(2)
C.stop()