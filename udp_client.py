from __future__ import annotations
import socket
from threading import Thread
from typing import Optional
from Message import *
import hashlib


class UDPClient:

    def __init__(self, ip_local: str, port: int, ip_server: str, port_server, password: Optional[str] = "") -> None:
        self.ip_local: str = ip_local
        self.port: int = port
        self.ip_server: str = ip_server
        self.port_server = port_server
        self.hash_pass = hashlib.sha1(bytes(password, "utf8")).hexdigest()
        self.listener = self.Listener(self.ip_local, self.port, ip_server, port_server, self.hash_pass)

    def start(self) -> None:
        self.listener.start()

    def stop(self) -> None:
        self.listener.stop()

    def send(self, message: str, message_id: Optional[int] = 0):
        # if message_id == 1:

        self.listener.send(message, message_id)

    class Listener(Thread):

        def __init__(self, ip: str, port: int, ip_server: str, port_server, hash_pass: str) -> None:
            Thread.__init__(self)
            self.is_running: bool = False
            self.ip: str = ip
            self.port: int = port
            self.socket: socket.socket = socket.socket(socket.AF_INET,  # Internet
                                                       socket.SOCK_DGRAM)  # UDP
            self.hash_pass = hash_pass

            self.client_is_connected: bool = False
            self.client_ip: str = ip_server
            self.client_port: int = port_server
            # ===========

            self.send_socket = socket.socket(socket.AF_INET,  # Internet
                                             socket.SOCK_DGRAM)

        def listen(self) -> None:
            """
            Infinite loop for the server
            :return:
            None
            """
            self.socket.bind((self.ip, self.port))
            while self.is_running:
                self.connection()  # wait for connection

                """
                Start Listening 
                """
                data, addr = self.socket.recvfrom(2048)  # buffer size is 1024 bytes

                # DEBUG A ENLEVER PLUS TARD
                data_string = data.decode("utf-8")

                last_message = Message.check_message(data_string)

        def connection(self):
            """
            Send connexion request while it receive no CONNECTED answer
            :return:
            None
            """
            while not self.client_is_connected:
                self.send('{"port" : 50054, "pass" : "' + self.hash_pass + '"}', 1)
                data, addr = self.socket.recvfrom(2048)  # buffer size is 1024 bytes

                # DEBUG A ENLEVER PLUS TARD
                data_string = data.decode("utf-8")
                try:
                    message = Message.create_json(data_string)
                except ValueError:
                    print("Validation KO")
                    message = Message(0, "")
                if message.verif():
                    print("received message:", message.message)
                    if message.id == 2:
                        if "answer" in message.content:
                            self.client_is_connected = True
                        else:
                            print("Rebellotte")

        def run(self) -> None:
            """
            Start the listener
            :return:
            """
            self.is_running = True
            self.listen()

        def stop(self) -> None:
            """
            Stop the listener
            :return:
            """
            self.is_running = False

        def send(self, message: str, message_id: Optional[int] = 0):
            """
            Send a message to the client
            :param message:
            The string to send
            :param message_id:
            The id of the message (default = 0)
            :return:
            None
            """
            datas_to_send = Message(message_id, message)
            self.socket.sendto(bytes(str(datas_to_send), 'utf-8'), (self.client_ip, self.client_port))
