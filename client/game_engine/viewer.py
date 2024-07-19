from abc import ABC, abstractmethod
import pygame
from game_engine.scene import Scene


class Viewer(ABC):
    def __init__(self, scene: Scene) -> None:
        self._scene: Scene = scene
    
    def set_scene(self, new_scene: Scene) -> None:
        assert isinstance(new_scene, Scene), Exception('In argument must be scene')
        self._scene = new_scene

    @abstractmethod 
    def display(self, screen: pygame.Surface) -> None:
        pass
