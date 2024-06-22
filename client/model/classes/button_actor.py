from model.source.actor import Actor
from typing import Tuple, Callable
import pygame


class ButtonActor(Actor):
    def __init__(self, rect: pygame.Rect, color: pygame.Color, callback: Callable) -> None:
        self.rect: pygame.Rect = rect
        self.color: pygame.Color = color
        self.callback: Callable = callback
    

    def click(self, cursor_pos: Tuple[int, int]):
        if self.rect.collidepoint(cursor_pos):
            self.callback()
