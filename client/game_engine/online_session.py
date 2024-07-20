import socket
from typing import Tuple, Dict, Any, Optional
import json


class OnlineSession:
    def __init__(self, server_host: str = '127.0.0.1', server_port: int = 7000) -> None:
        self.connection: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address: Tuple[str, int] = (server_host, server_port)
    
    def send(self, data: Dict[str, Any]) -> None:
        self.connection.sendto(json.dumps(data).encode(), self.server_address)
    
    def get(self) -> Optional[Dict[str, Any]]:
        data: bytes
        address: Tuple[str, int]
        data, address = self.connection.recvfrom(1024)

        if address == self.server_address:
            return json.loads(data)
        
        return None
