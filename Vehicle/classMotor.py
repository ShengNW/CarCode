from machine import Pin, PWM
import time
class Servo:
    def __init__(self, pin, freq):
        self.pin = PWM(Pin(pin, Pin.OUT),freq=freq)
        self.turn(50)
        
    def turn(self, angle):
        value = int(500 + (angle/100)*(2500-500))
        self.pin.duty_ns(value*1000)
        
        
        
# class Motor:
#     def __init__(self, pin, freq):
#         self.pin = PWM(Pin(pin, Pin.OUT),freq=freq)
#         self.pin.duty(77)
#         
#     def go(self, angle):
#         self.pin.duty(angle)
# #         value = int(500 + (angle/100)*(2500-500))
# #         self.pin.duty_ns(value*1000)
#     def stop(self):
#         self.pin.duty(0)
class Motor:
    def __init__(self, pin, freq):
        self.pwm = PWM(Pin(pin, Pin.OUT), freq=freq)  # Renamed to pwm for clarity
        self.pwm.duty(77)
        
    def go(self, angle):
        self.pwm.duty(angle)
        
    def stop(self):
        self.pwm.duty(0)
