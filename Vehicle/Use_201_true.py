from classMotor_200_OneFunc import *
from machine import Pin, PWM
import time

A = Servo(18,50)
B = Motor(33,25,50)
#A.turn(100)

# B.go(200)
# time.sleep(1)
# B.back(128)
# time.sleep(1)
# B.stop()

B.go(800)
time.sleep(1)
B.back(800)
time.sleep(1)
B.stop()
# B.go(200)
# time.sleep(1)
# A.right()
# B.stop()
# time.sleep(2)
# B.go(200)
# time.sleep(2)
# print("to 1")
# B.back(128)
# time.sleep(2)
# A.left()
# B.stop()
# time.sleep(2)
# B.go(200)
# time.sleep(2)
# print("to 2")
# B.back(128)
# time.sleep(2)
# B.stop()