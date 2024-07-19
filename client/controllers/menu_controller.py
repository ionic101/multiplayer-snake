from game_engine.scene import Scene
from game_engine.controller import Controller, MouseButton
import pygame
import scenes.menu_scene as menu_scene
from typing import List, Tuple


class MenuController(Controller):
    def __init__(self, scene: Scene) -> None:
        super().__init__(scene)
        self.start_click: Tuple[int, int] = (-1, -1)
        self.end_click: Tuple[int, int] = (-1, -1)

    def control(self, events: List[pygame.event.Event]) -> None:
        super().control(events)

        if not isinstance(self._scene, menu_scene.MenuScene):
            return
        
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == MouseButton.LEFT.value:
                self.start_click = event.pos
            elif event.type == pygame.MOUSEBUTTONUP and event.button == MouseButton.LEFT.value:
                self.end_click = event.pos
                for button in self._scene.buttons:
                    if button.rect.collidepoint(self.start_click) and button.rect.collidepoint(self.end_click):
                        button.click()
        