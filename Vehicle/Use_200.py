from classMotor_200_OneFunc import *
from machine import Pin, PWM
import time
S1= Pin(33,Pin.IN)#PWM(Pin(25), freq=50, duty=0)
S1.value(1)


A = Servo(18,50)
time.sleep(2)
A.turn(20)
time.sleep(1)
A.turn(0)



B = Motor(33,25,50)
time.sleep(1)
B.go(128)
time.sleep(2)
B.stop()
time.sleep(1)
B.back(128)
time.sleep(2)
#print("to here")
B.stop()

# pin = PWM(Pin(18, Pin.OUT),freq=50)
# pin.duty(126)