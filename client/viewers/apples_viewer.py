import pygame
from game_engine.colors import Colors
from typing import List
import game_settings as settings
from pygame.math import Vector2


class ApplesViewer:
    @staticmethod
    def display(screen: pygame.Surface, apples: List[Vector2]) -> None:
        for apple in apples:
            pygame.draw.rect(screen,
                             Colors.RED.value,
                             pygame.Rect(apple.x * settings.CELL_WIDTH,
                                        apple.y * settings.CELL_WIDTH,
                                        settings.CELL_WIDTH,
                                        settings.CELL_WIDTH))