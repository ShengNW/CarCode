import socket
#from machine import Pin
#led = Pin(32, Pin.OUT)
from classMotor_200_OneFunc import *
from machine import Pin, PWM
import time

A = Servo(18,50)
B = Motor(33,25,50)


rate = 1000

def web_page():
    html = """<html><head><meta name = "viewport" content = "width=device-width, initial-scale=1"></head>
    <body>
    
    <h1>...</h1><a href=\"?led=on\"><button>ON</button></a>&nbsp;
    <p>Speed: <input type="range" min="0" max="1023" value="500" class="slider" id="speedSlider" oninput="updateSpeed(this.value)" /></p>
    
    <a href=\"?forward\"><button>Forward</button></a>&nbsp;
    <a href=\"?backward\"><button>Backward</button></a>&nbsp;

    
    
    <a href=\"?led=off\"><button>OFF</button></a></body><html>"""
    return html

    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.31.171", 8080))#192.168.31.83      192.168.31.172
s.listen(5)
print("Server is listening on port ")

while True:
    conn, addr = s.accept()
    print('Got a connection from %s'% str(addr))
    request = conn.recv(1024)
    #request = str(request)
    print('Content = %s \n'% str(request))#\n
    
    led_on = request.find(b'/?led=on')
    led_off = request.find(b'/?led=off')
    forward = request.find(b'/?forward')
    backward = request.find(b'/?backward')
    speed = request.find(b'/speed?value=')
    print(request.split(b'=')[1])
    print(request.split(b'=')[1].split(b' ')[0])
    print("**********",speed)
            # 更新速度
    #if request.find(b'/speed?value=') != -1:
    if speed == -1:
        speed_value = int(request.split(b'=')[1].split(b' ')[0])
        speed = speed_value
        print('Speed set to:', speed)
    if led_on ==4:#6
        print('LED ON')
        #led.value(1)
        A.right()
    elif led_off ==4:#6
        print('LED off')
        #led.value(0)
        A.left()
    
    elif forward ==4:#6
        print('LED off')
        #led.value(0)
        #A.left()
        B.go(rate)
        time.sleep(1)
        B.stop()
    
    elif backward ==4:#6
        print('LED off')
        #led.value(0)
        #A.right()
        B.back(rate)
        time.sleep(1)
        B.stop()
    
    response = web_page()
    conn.send(b'HTTP/1.1 200 OK\n')#\n
    conn.send(b"Content-Type: text/html\n")#\n
    conn.send(b'Connection: close\n\n')#\n
    conn.sendall(response.encode())

    conn.close()
    

