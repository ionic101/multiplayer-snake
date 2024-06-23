from abc import ABC
from pygame.math import Vector2
import pygame
from model.source.colors import Colors


class Actor(ABC):
    def __init__(self, coord: Vector2) -> None:
        self.coord = coord
