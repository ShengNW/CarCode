from machine import Pin, PWM
import time
class Servo:
    def __init__(self, pin, freq):
        self.pin = PWM(Pin(pin, Pin.OUT),freq=freq)
        self.turn(90)
        
    def turn(self, angle):
        value = int(500 + (angle/100)*(2500-500))
        self.pin.duty_ns(value*1000)
        
    def right(self):
        self.turn(100)
    def left(self):
        self.turn(0)
    def zero(self):
        self.turn(90)
class Motor:
    def __init__(self, pin, pin2, freq):
        self.pwm = PWM(Pin(pin, Pin.OUT), freq=freq)  # Renamed to pwm for clarity
        self.pwm.duty(77)
        self.pwm2 = PWM(Pin(pin2, Pin.OUT), freq=freq)  # Renamed to pwm for clarity
        self.pwm2.duty(77)
        
    def go(self, angle):
        self.pwm2.duty(0)
        self.pwm.duty(angle)
        
    def stop(self):
        #print("to here")
        self.pwm.duty(0)
        self.pwm2.duty(0)
        
    def back(self,angle):
        #print("to here")
        self.pwm.duty(0)
        self.pwm2.duty(angle)