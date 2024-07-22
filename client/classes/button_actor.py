from game_engine.actor import Actor
from typing import Callable, Any
import pygame
from pygame.math import Vector2


class ButtonActor(Actor):
    def __init__(self, rect: pygame.Rect, text: str = '', text_size: int = 40, callback: Callable[..., Any] = lambda: None) -> None:
        super().__init__(Vector2(rect.x, rect.y))
        self.width = rect.width
        self.height = rect.height
        self.rect: pygame.Rect = rect
        self.text: str = text
        self.text_size: int = text_size
        self.callback: Callable[..., Any] = callback

    def click(self):
        self.callback()
