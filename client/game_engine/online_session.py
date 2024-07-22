import socket
from typing import Tuple, Dict, Any, Optional
import json
import asyncio


class OnlineSession:
    def __init__(self, server_host: str = '127.0.0.1', server_port: int = 7000) -> None:
        self.connection: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.connection.setblocking(False)  # Устанавливаем неблокирующий режим
        self.server_address: Tuple[str, int] = (server_host, server_port)
    
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
