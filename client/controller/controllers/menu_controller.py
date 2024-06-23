from model.classes.snake_actor import SnakeActor
from model.source.scene import Scene
from controller.controller import Controller
from typing import Callable, List
import pygame
from pygame.math import Vector2
from model.scenes.menu_scene import MenuScene


class MenuController(Controller):
    def __init__(self, scene: Scene, stop_game_action: Callable) -> None:
        super().__init__(scene, stop_game_action)
    

    def update(self) -> None:
        super().update()

        if not isinstance(self._scene, MenuScene):
            return
        
        if pygame.mouse.get_pressed()[0]:
            for button in self._scene.buttons:
                button.click(pygame.mouse.get_pos())
