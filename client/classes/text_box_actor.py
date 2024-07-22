from game_engine.actor import Actor
import pygame
from pygame.math import Vector2


class TextBoxActor(Actor):
    def __init__(self, rect: pygame.Rect, text: str = '', text_size: int = 20) -> None:
        super().__init__(Vector2(rect.x, rect.y))
        self.text: str = text
        self.text_size: int = text_size
        self.width = rect.width
        self.height = rect.height
        self.rect: pygame.Rect = rect
        self.is_active: bool = False
    
    def append(self, letter: str) -> None:
        self.text += letter
    
    def backspace(self) -> None:
        self.text = self.text[:-1]

    def activate(self) -> None:
        self.is_active = True

    def incactivate(self) -> None:
        self.is_active = False
