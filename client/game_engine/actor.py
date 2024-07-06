from abc import ABC
from pygame.math import Vector2


class Actor(ABC):
    def __init__(self, coord: Vector2) -> None:
        self.coord = coord
