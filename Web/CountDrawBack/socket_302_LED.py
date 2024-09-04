import socket
from machine import Pin
led = Pin(32, Pin.OUT)
# def web_page():
#     html = """<html><head><meta name = "viewport" content = "width= device-width, initial-scale= 1"></head>
#     <body>
#     <h1>...</h1><a href=\"?led=on"><button>ON</button></a>&nbsp;
#     <a href=\"?led=off\"><button>OFF</button></a></body><html>"""
def web_page():
    html = """<html><head><meta name = "viewport" content = "width=device-width, initial-scale=1"></head>
    <body>
    <h1>...</h1><a href=\"?led=on\"><button>ON</button></a>&nbsp;
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
    print("**********",led_on)
    if led_on ==4:#6
        print('LED ON')
        led.value(1)
    elif led_off ==4:#6
        print('LED off')
        led.value(0)
    
    response = web_page()
    conn.send(b'HTTP/1.1 200 OK\n')#\n
    conn.send(b"Content-Type: text/html\n")#\n
    conn.send(b'Connection: close\n\n')#\n
    #conn.sendall(response)
    conn.sendall(response.encode())

    conn.close()
    