import pygame
from game_engine.scene import Scene
from game_engine.viewer import Viewer


class BaseViewer(Viewer):
    def __init__(self, scene: Scene) -> None:
        super().__init__(scene)

    def display(self, screen: pygame.Surface) -> None:
        pass
