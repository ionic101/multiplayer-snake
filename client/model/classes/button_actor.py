from model.source.actor import Actor
from typing import Tuple, Callable
import pygame
from pygame.math import Vector2
from model.source.colors import Colors


class ButtonActor(Actor):
    def __init__(self, rect: pygame.Rect, text: str = '', callback: Callable = lambda: None) -> None:
        super().__init__(Vector2(rect.x, rect.y))
        self.width = rect.width
        self.height = rect.height
        self.rect: pygame.Rect = rect
        self.text: str = text
        self.callback: Callable = callback
    

    def click(self, cursor_pos: Tuple[int, int]):
        if self.rect.collidepoint(cursor_pos):
            self.callback()
