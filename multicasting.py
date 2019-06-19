from udp_client import *
import time

bool = True

server = UDPClient("127.0.0.1", 50057, "127.0.0.1", 50055, "test")
server.start()
# i = 0
# while i < 100:
#     server.send('{"port" : 50055, "pass" : "' + server.hash_pass + '"}', 1)
#     i += 1
