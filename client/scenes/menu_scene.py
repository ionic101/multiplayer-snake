from game_engine.scene import Scene
from typing import List
import pygame
import game_settings as game_settings
from classes.button_actor import ButtonActor
from game_engine.game_engine import GameEngine



class MenuScene(Scene):
    def __init__(self) -> None:
        self._BUTTON_WIDTH: int = 300
        self._BUTTON_HEIGHT: int = 70
        self._BUTTOM_INTERVAL: int = 100

        self.buttons: List[ButtonActor] = [
            ButtonActor(
                rect=pygame.Rect(
                    game_settings.SCREEN_WIDTH // 2 - self._BUTTON_WIDTH // 2,
                    game_settings.SCREEN_HEIGHT // 2 - self._BUTTON_HEIGHT // 2,
                    self._BUTTON_WIDTH,
                    self._BUTTON_HEIGHT
                ),
                text='singleplayer',
                callback=lambda: print('singleplayer')
            ),
            ButtonActor(
                rect=pygame.Rect(
                    game_settings.SCREEN_WIDTH // 2 - self._BUTTON_WIDTH // 2,
                    game_settings.SCREEN_HEIGHT // 2 - self._BUTTON_HEIGHT // 2 + self._BUTTOM_INTERVAL,
                    self._BUTTON_WIDTH,
                    self._BUTTON_HEIGHT
                ),
                text='multiplayer',
                callback=lambda: print('multiplayer')
            ),
            ButtonActor(
                rect=pygame.Rect(
                    game_settings.SCREEN_WIDTH // 2 - self._BUTTON_WIDTH // 2,
                    game_settings.SCREEN_HEIGHT // 2 - self._BUTTON_HEIGHT // 2 + self._BUTTOM_INTERVAL * 2,
                    self._BUTTON_WIDTH,
                    self._BUTTON_HEIGHT
                ),
                text='quit',
                callback=GameEngine.quit
            ),
        ]
