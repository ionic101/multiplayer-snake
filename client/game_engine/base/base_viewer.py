import pygame
from game_engine.scene import Scene
from game_engine.viewer import Viewer


class BaseViewer(Viewer):
    def __init__(self, screen: pygame.Surface, scene: Scene) -> None:
        super().__init__(screen, scene)
    

    def display(self) -> None:
        pass
