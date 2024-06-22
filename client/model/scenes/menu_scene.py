from model.source.scene import Scene
from model.classes.button_actor import ButtonActor
from typing import List
import pygame


class MenuScene(Scene):
    def __init__(self) -> None:
        self.buttons: List[ButtonActor] = [
            ButtonActor(pygame.Rect(10, 10, 100, 50), pygame.Color(255, 0, 0), lambda: print('Hello world!')),
            ButtonActor(pygame.Rect(210, 10, 200, 50), pygame.Color(255, 0, 0), lambda: print('Hello world2!'))
        ]
