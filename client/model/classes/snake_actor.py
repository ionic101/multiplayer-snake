from model.source.actor import Actor
from pygame.math import Vector2
from model.source.direction import Direction


class SnakeActor(Actor):
    def __init__(self, coord: Vector2) -> None:
        self.coord = coord
    

    def move(self, direction: Direction) -> None:
        self.coord += direction
