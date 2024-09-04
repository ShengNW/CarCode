import socket
#from machine import Pin
#led = Pin(32, Pin.OUT)
from classMotor_200_OneFunc import *
from machine import Pin, PWM
import time
A = Servo(18, 50)
B = Motor(33, 25, 50)
rate = 1000
def web_page():
    html = f"""<html>
    <head>
        <meta name = "viewport" content = "width=device-width, initial-scale=1">
    </head>
    <body>
        <h1>Control Panel</h1>
        <a href=\"?led=on\"><button>ON</button></a>&nbsp;
        <a href=\"?forward\"><button>Forward</button></a>&nbsp;
        <a href=\"?backward\"><button>Backward</button></a>&nbsp;
        <a href=\"?led=off\"><button>OFF</button></a>
        
        <h2>Set Speed:</h2>
        <input type="range" min="0" max="1000" value="{rate}" id="speedSlider" onchange="updateSpeed(this.value)">
        <p>Speed: <span id="speedValue">{rate}</span></p>
        <script>
            function updateSpeed(value) {{
                document.getElementById("speedValue").innerHTML = value;
                fetch("?speed=" + value); // Send the speed to the server
            }}
        </script>
    </body>
    </html>"""
    return html
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.31.171", 8080))  # 192.168.31.83      192.168.31.172
s.listen(5)
print("Server is listening on port 8080")
while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    print('Content = %s \n' % str(request))  # \n
    led_on = request.find(b'/?led=on')
    led_off = request.find(b'/?led=off')
    forward = request.find(b'/?forward')
    backward = request.find(b'/?backward')
    speed_request = request.find(b'?speed=')
    if led_on == 4:  # 6
        print('LED ON')
        A.right()
    elif led_off == 4:  # 6
        print('LED off')
        A.left()
    elif forward == 4:  # 6
        print('Moving Forward')
        B.go(rate)
        time.sleep(1)
        B.stop()
    elif backward == 4:  # 6
        print('Moving Backward')
        B.back(rate)
        time.sleep(1)
        B.stop()
    elif speed_request != -1:  # If a speed change request was made
        speed_value = request.split(b'?speed=')[1]
        rate = int(speed_value.split(b' ')[0])  # Extract the speed value
        print(f'Speed changed to: {rate}')
    response = web_page()
    conn.send(b'HTTP/1.1 200 OK\n')  # \n
    conn.send(b"Content-Type: text/html\n")  # \n
    conn.send(b'Connection: close\n\n')  # \n
    conn.sendall(response.encode())
    conn.close()