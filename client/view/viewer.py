from abc import ABC, abstractmethod
import pygame


class Viewer(ABC):
    def __init__(self, screen: pygame.Surface):
        self._screen: pygame.Surface = screen


    @abstractmethod 
    def display(self):
        pass
