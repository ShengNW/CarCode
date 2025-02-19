try:
    import usocket as socket
except:
    import socket
    
import network
import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = '图克-601-5G'
password = 'tuke666888'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
    pass

print('Connection successful')
print(station.ifconfig())