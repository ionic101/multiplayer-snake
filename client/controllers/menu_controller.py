from game_engine.scene import Scene
from game_engine.controller import Controller
import pygame
from scenes.menu_scene import MenuScene
from typing import List


class MenuController(Controller):
    def __init__(self, scene: Scene) -> None:
        super().__init__(scene)

    def control(self, events: List[pygame.event.Event]) -> None:
        super().control(events)

        if not isinstance(self._scene, MenuScene):
            return
        
        if pygame.mouse.get_pressed()[0]:
            for button in self._scene.buttons:
                button.click(pygame.mouse.get_pos())
