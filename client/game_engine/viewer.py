from abc import ABC, abstractmethod
import pygame
from game_engine.scene import Scene


class Viewer(ABC):
    def __init__(self, screen: pygame.Surface, scene: Scene):
        self._screen: pygame.Surface = screen
        self._scene: Scene = scene
    

    @abstractmethod 
    def display(self) -> None:
        pass
