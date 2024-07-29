import socket
import threading
from typing import Optional, Dict, Any
import json
import time


class Player:
    def __init__(self, address: tuple[str, int], connection: socket.socket):
        self.address: tuple[str, int] = address
        self.connection: socket.socket = connection
    
    def connect(self, status: bool = True) -> None:
        data: Dict[str, Any] = {
            'type': 'connect',
            'status': status,
            'message': ''
        }
        self.connection.sendto(json.dumps(data).encode(), self.address)


class GameServer:
    def __init__(self, ip: str = '127.0.0.1', port: int = 7000) -> None:
        self.ip: str = ip
        self.port: int = port
        self._socket: Optional[socket.socket] = None
        self._players: dict[tuple[str, int], Player] = {}

    def __create_socket(self) -> None:
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._socket.setblocking(False)
        self._socket.bind((self.ip, self.port))

    def __parse_request(self, request: bytes, address: tuple[str, int]) -> None:
        assert self._socket is not None, 'Socket is not init'
        
        data = json.loads(request.decode())
        print(data)

        if data['type'] == 'connect':
            player: Player = Player(address, self._socket)
            self._players[address] = player
            player.connect()

    def __listen(self) -> None:
        while self.is_run():
            try:
                if self._socket:
                    self.__parse_request(*self._socket.recvfrom(1024))
            except socket.error:
                pass
            time.sleep(0.01)

    def run(self) -> None:
        self.__create_socket()
        threading.Thread(target=self.__listen).start()

    def stop(self) -> None:
        if self._socket is not None:
            self._socket.close()
        self._socket = None

    def is_run(self) -> bool:
        return self._socket is not None

    def get_address(self) -> str:
        return str(self.ip) + ':' + str(self.port)
