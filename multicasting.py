from udp_client import *
import time

bool = True

server = UDPClient("192.168.43.184", 50057, "192.168.43.154", 50055, "test")
server.start()
# i = 0
# while i < 100:
#     server.send('{"port" : 50055, "pass" : "' + server.hash_pass + '"}', 1)
#     i += 1
