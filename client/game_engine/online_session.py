import socket
from typing import Tuple, Dict, Any, Optional
import json
import asyncio
import re


class OnlineSession:
    def __init__(self, server_host: str = '127.0.0.1', server_port: int = 7000) -> None:
        self.connection: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.connection.setblocking(False)
        self.server_address: Tuple[str, int] = (server_host, server_port)

    @staticmethod
    def is_address_valid(address: str):
        ip_port_regex = re.compile(
            r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}'
            r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
            r':(6553[0-5]|655[0-2][0-9]|65[0-4][0-9][0-9]|6[0-4][0-9]{3}|'
            r'[1-5][0-9]{4}|[0-9]{1,4})$'
        )
        
        return bool(ip_port_regex.match(address))
    
    def set_address(self, address: str) -> None:
        assert self.is_address_valid(address), 'Invalid address format'
        ip, port = address.split(':')
        self.server_address = (ip, int(port))
    
    def send(self, data: Dict[str, Any]) -> None:
        self.connection.sendto(json.dumps(data).encode(), self.server_address)
    
    async def _get_async(self) -> Optional[Dict[str, Any]]:
        loop = asyncio.get_running_loop()
        try:
            data, address = await loop.sock_recvfrom(self.connection, 1024)
            if address == self.server_address:
                return json.loads(data)
        except (asyncio.IncompleteReadError, OSError):
            return None

    def get(self) -> Optional[Dict[str, Any]]:
        return asyncio.run(self._get_async())
