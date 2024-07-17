from abc import ABC
from pygame.math import Vector2


class Actor(ABC):
    def __init__(self, coord: Vector2) -> None:
        self._coord: Vector2 = coord

    @property
    def coord(self) -> Vector2:
        return self._coord
    
    @coord.setter
    def coord(self, new_coord: Vector2) -> None:
        self._coord: Vector2 = new_coord
