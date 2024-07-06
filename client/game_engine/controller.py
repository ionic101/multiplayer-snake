from abc import ABC
from game_engine.scene import Scene
import pygame
import game_engine.game_engine


class Controller(ABC):
    def __init__(self, scene: Scene) -> None:
        self._scene = scene
    

    def control(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_engine.GameEngine.quit()
