from model.source.actor import Actor
from pygame.math import Vector2
from model.source.direction import Direction
import pygame
from model.source.colors import Colors


class SnakeActor(Actor):
    def __init__(self, coord: Vector2) -> None:
        super().__init__(coord)
        self.coord = coord
    

    def move(self, direction: Direction) -> None:
        self.coord += direction
