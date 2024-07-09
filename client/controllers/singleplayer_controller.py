from game_engine.scene import Scene
from game_engine.controller import Controller
from scenes.singleplayer_scene import SingleplayerScene
import pygame
from game_engine.direction import Direction
from typing import List


class SingleplayerController(Controller):
    def __init__(self, scene: Scene) -> None:
        super().__init__(scene)
    

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
