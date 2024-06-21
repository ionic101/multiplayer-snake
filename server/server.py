import socket
import threading
from typing import Optional
import json

class Player:
    def __init__(self, address: tuple[str, int]):
        self.address = address
    

class Server:
    def __init__(self, ip: str = '127.0.0.1', port: int = 7000):
        self.ip: str = ip
        self.port: int = port
        self.is_run: bool = False
        self._socket: Optional[socket.socket]

        self._players: dict[tuple[str, int], Player] = {}
    
    def __create_socket(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._socket.setblocking(False)
        self._socket.bind((self.ip, self.port))
    
    @staticmethod
    def get_decoded_request(request: bytes) -> dict[str, str]:
        decoded_request: dict[str, str] = {}
        param: str
        value: str
        for data in request.decode().split('&'):
            param, value = data.split('=')
            decoded_request[param] = value
        
        return decoded_request
    
    def __parse_request(self, request: bytes, address: tuple[str, int]):
        data = json.loads(request.decode())
        print(data)

        if data['command'] == 'connect':
            player: Player = Player(address)
            self._players[address] = player

    def __listen(self):
        assert self._socket, 'Socket doesn\'t exist'
        while self.is_run:
            try:
                self.__parse_request(*self._socket.recvfrom(1024))
            except socket.error:
                continue
    
    def run(self):
        self.is_run = True
        self.__create_socket()
        threading.Thread(target=self.__listen).start()
        
    
    def stop(self):
        self.is_run = False
        self._socket.close()
