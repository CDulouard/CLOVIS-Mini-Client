from udp_client import *
import time

bool = True

server = UDPClient("192.168.43.184", 50057, "192.168.43.154", 50055, "test")
server.start()
# i = 0
# while i < 100:
#     server.send('{"port" : 50055, "pass" : "' + server.hash_pass + '"}', 1)
#     i += 1

# while True:
#     if server.check_connection():
#         for i in range(5):
#             server.send('{"torsoRY": -10}', 5)
#             time.sleep(0.2)
#         for i in range(5):
#             server.send("{}", 3)
#             time.sleep(0.2)
#         break

tmp = 0
while True:
    if server.check_connection():

        server.send('{"torsoRY": ' + str(tmp) + '}', 5)
        time.sleep(0.05)
        tmp += 10
