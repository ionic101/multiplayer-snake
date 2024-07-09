from game_engine.controller import Controller
from game_engine.scene import Scene
import pygame
from typing import List


class BaseController(Controller):
    def __init__(self, scene: Scene) -> None:
        super().__init__(scene)
    
    def control(self, events: List[pygame.event.Event]) -> None:
        super().control(events)
