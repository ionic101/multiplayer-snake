from abc import ABC, abstractmethod
from model.source.game_session_data import GameSessionData
import pygame
from model.source.scene import Scene


class Viewer(ABC):
    def __init__(self, screen: pygame.Surface, scene: Scene):
        self._screen: pygame.Surface = screen
        self._scene: Scene = scene


    @abstractmethod 
    def display(self):
        pass
