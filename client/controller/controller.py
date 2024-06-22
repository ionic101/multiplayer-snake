from abc import ABC
from model.source.scene import Scene
from typing import Callable
import pygame


class Controller(ABC):
    def __init__(self, scene: Scene, stop_game_action: Callable) -> None:
        self._scene = scene
        self._stop_game_action: Callable = stop_game_action
    

    def update(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._stop_game_action()
