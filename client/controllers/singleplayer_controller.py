from game_engine.scene import Scene
from game_engine.controller import Controller, MouseButton
from scenes.singleplayer_scene import SingleplayerScene
import pygame
from game_engine.direction import Direction
from typing import List, Tuple
from scenes.singleplayer_scene import GameStatus


class SingleplayerController(Controller):
    def __init__(self, scene: Scene) -> None:
        super().__init__(scene)
        self.start_click: Tuple[int, int] = (-1, -1)
        self.end_click: Tuple[int, int] = (-1, -1)

    def control(self, events: List[pygame.event.Event]) -> None:
        super().control(events)
        
        if not isinstance(self._scene, SingleplayerScene):
            return
        
        for event in events:
            if event.type == pygame.KEYDOWN:
                key = event.key
                if key == pygame.K_a:
                    self._scene.snake.set_direction(Direction.LEFT)
                elif key == pygame.K_d:
                    self._scene.snake.set_direction(Direction.RIGHT)
                elif key == pygame.K_w:
                    self._scene.snake.set_direction(Direction.UP)
                elif key == pygame.K_s:
                    self._scene.snake.set_direction(Direction.DOWN)
                elif key == pygame.K_ESCAPE:
                    if self._scene.game_status == GameStatus.PLAY:
                        self._scene.game_status = GameStatus.PAUSE
                    elif self._scene.game_status == GameStatus.PAUSE:
                        self._scene.game_status = GameStatus.PLAY
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == MouseButton.LEFT.value:
                self.start_click = event.pos
            elif event.type == pygame.MOUSEBUTTONUP and event.button == MouseButton.LEFT.value:
                self.end_click = event.pos
                for button in self._scene.buttons:
                    if button.rect.collidepoint(self.start_click) and button.rect.collidepoint(self.end_click):
                        button.click()
