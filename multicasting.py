from udp_client import *
import time

bool = True

server = UDPClient("192.168.50.90", 50057, "192.168.50.1", 50056, "test")
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
        # server.send('{"rAnkleRX": ' + str(tmp - 180) + ', "lAnkleRX":' + str(
        #     tmp - 180) + ', "rAnkleRZ":' + str(tmp - 180) + ', "lAnkleRZ":' + str(tmp - 180) + ', "rShoulderRY":' + str(
        #     tmp - 180) + ', "lShoulderRY":' + str(tmp - 180) + ', "rShoulderBaseRY":' + str(
        #     tmp - 180) + ', "lShoulderBaseRY":' + str(
        #     tmp - 180) + ', "rShoulderRZ":' + str(tmp - 180) + ', "lShoulderRZ":' + str(
        #     tmp - 180) + ', "rKneeRX":' + str(tmp - 180) + ', "lKneeRX":' + str(tmp - 180) + '}', 5)

        # server.send('{"rAnkleRX": ' + str(tmp - 180) + ', "lAnkleRX":' + str(
        #     tmp - 180) + ', "rAnkleRZ":' + str(tmp - 180) + ', "lAnkleRZ":' + str(tmp - 180) + '}', 5)

        # server.send('{"rElbowRX":' + str(tmp - 180) + '}', 5)

        # server.send('{"rAnkleRX": ' + str(tmp - 180) + ', "lAnkleRX":' + str(
        #     tmp - 180) + ', "rAnkleRZ":' + str(tmp - 180) + ', "lAnkleRZ":' + str(tmp - 180) + ', "rShoulderRY":' + str(
        #     tmp - 180) + ', "rShoulderBaseRY":' + str(tmp - 180) + ', "lShoulderBaseRY":' + str(
        #     tmp - 180) + ', "lShoulderRY":' + str(tmp - 180) + ', "rShoulderRZ":' + str(
        #     tmp - 180) + ', "lShoulderRZ":' + str(tmp - 180) + ', "rKneeRX":' + str(tmp - 180) + ', "lKneeRX":' + str(
        #     tmp - 180) + ', "rHipRX":' + str(tmp - 180) + ', "lHipRX":' + str(tmp - 180) + ', "rHipRY":' + str(
        #     tmp - 180) + ', "lHipRY":' + str(tmp - 180) + ', "rHipRZ":' + str(tmp - 180) + ', "lHipRZ":' + str(
        #     tmp - 180) + ', "headRX":' + str(tmp - 180) + ', "rElbowRX":' + str(tmp - 180) + ', "lElbowRX":' + str(
        #     tmp - 180) + ', "torsoRY":' + str(tmp - 180) + '}', 5)

        # server.send('{"rElbowRX":' + str(0) + '}', 5)
        # time.sleep(0.5)
        # server.send('{"rElbowRX":' + str(-50) + '}', 5)
        # time.sleep(0.5)
        # server.send('{"rElbowRX":' + str(-100) + '}', 5)
        # time.sleep(0.5)
        # server.send('{"rElbowRX":' + str(-50) + '}', 5)
        # time.sleep(0.5)
        # tmp = (tmp + 50) % 300

        # server.send('{"rShoulderRZ":' + str(0) + '}', 5)
        # time.sleep(1)
        # server.send('{"rShoulderRZ":' + str(-100) + '}', 5)
        # time.sleep(1)

        # server.send('{"lShoulderRZ":' + str(0) + '}', 5)
        # time.sleep(1)
        # server.send('{"lShoulderRZ":' + str(100) + '}', 5)
        # time.sleep(1)

        # server.send('{"rShoulderRZ": ' + str(0) + ', "lShoulderRZ":' + str(
        #     0) + '}', 5)
        # time.sleep(1)
        # server.send('{"rShoulderRZ": ' + str(-100) + ', "lShoulderRZ":' + str(
        #     100) + '}', 5)
        # time.sleep(1)

        POSI = 1
        server.send('{"rAnkleRX": ' + str(POSI) + ', "lAnkleRX":' + str(
            POSI) + ', "rAnkleRZ":' + str(POSI) + ', "lAnkleRZ":' + str(POSI) + ', "rShoulderRY":' + str(
            POSI) + ', "rShoulderBaseRY":' + str(POSI) + ', "lShoulderBaseRY":' + str(
            POSI) + ', "lShoulderRY":' + str(POSI) + ', "rShoulderRZ":' + str(
            POSI) + ', "lShoulderRZ":' + str(POSI) + ', "rKneeRX":' + str(POSI) + ', "lKneeRX":' + str(
            POSI) + ', "rHipRX":' + str(POSI) + ', "lHipRX":' + str(POSI) + ', "rHipRY":' + str(
            POSI) + ', "lHipRY":' + str(POSI) + ', "rHipRZ":' + str(POSI) + ', "lHipRZ":' + str(
            POSI) + ', "rElbowRX":' + str(POSI) + ', "lElbowRX":' + str(
            POSI) + ', "torsoRY":' + str(POSI) + '}', 5)

        time.sleep(1)

        # server.send('{"rKneeRX":' + str(0) + '}', 5)
        # time.sleep(1)
        # server.send('{"rKneeRX":' + str(60) + '}', 5)
        # time.sleep(1)

        # server.send('{"rHipRZ":' + str(0) + '}', 5)
        # time.sleep(1)
        # server.send('{"lHipRZ":' + str(0) + '}', 5)
        # time.sleep(1)
        # server.send('{"rHipRZ":' + str(10) + '}', 5)
        # time.sleep(1)