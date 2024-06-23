from model.source.scene import Scene
from model.classes.button_actor import ButtonActor
from typing import List, Tuple
import pygame
from model.source.colors import Colors
import settings
from typing import Callable


class MenuScene(Scene):
    def __init__(self, stop_game_action: Callable) -> None:
        self._BUTTON_WIDTH: int = 300
        self._BUTTON_HEIGHT: int = 70
        self._BUTTOM_INTERVAL: int = 100


        self.buttons: List[ButtonActor] = [
            ButtonActor(
                rect=pygame.Rect(
                    settings.SCREEN_WIDTH // 2 - self._BUTTON_WIDTH // 2,
                    settings.SCREEN_HEIGHT // 2 - self._BUTTON_HEIGHT // 2,
                    self._BUTTON_WIDTH,
                    self._BUTTON_HEIGHT
                ),
                text='singleplayer',
                callback=lambda: print('singleplayer')
            ),
            ButtonActor(
                rect=pygame.Rect(
                    settings.SCREEN_WIDTH // 2 - self._BUTTON_WIDTH // 2,
                    settings.SCREEN_HEIGHT // 2 - self._BUTTON_HEIGHT // 2 + self._BUTTOM_INTERVAL,
                    self._BUTTON_WIDTH,
                    self._BUTTON_HEIGHT
                ),
                text='multiplayer',
                callback=lambda: print('multiplayer')
            ),
            ButtonActor(
                rect=pygame.Rect(
                    settings.SCREEN_WIDTH // 2 - self._BUTTON_WIDTH // 2,
                    settings.SCREEN_HEIGHT // 2 - self._BUTTON_HEIGHT // 2 + self._BUTTOM_INTERVAL * 2,
                    self._BUTTON_WIDTH,
                    self._BUTTON_HEIGHT
                ),
                text='quit',
                callback=stop_game_action
            ),
        ]
