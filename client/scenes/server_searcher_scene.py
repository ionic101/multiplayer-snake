from game_engine.scene import Scene
from classes.text_box_actor import TextBoxActor
from classes.button_actor import ButtonActor
import pygame
import game_settings as settings
from random import randint
from typing import List
import scenes.menu_scene as menu_scene
import viewers.menu_viewer as menu_viewer
import controllers.menu_controller as menu_controller
from game_engine.game_engine import GameEngine
from game_engine.online_session import OnlineSession


class ServerSearcherScene(Scene):
    def __init__(self) -> None:
        super().__init__()

        self.online_session: OnlineSession = OnlineSession()

        self.TEXT_BOX_WIDTH: int = 500
        self.TEXT_BOX_HEIGHT: int = 70
        self.BUTTON_WIDTH: int = 210
        self.BUTTON_HEIGHT: int = 70

        self.nickname_text_box: TextBoxActor = TextBoxActor(
            pygame.Rect(
                settings.SCREEN_WIDTH // 2 - self.TEXT_BOX_WIDTH // 2,
                240,
                self.TEXT_BOX_WIDTH,
                self.TEXT_BOX_HEIGHT
            ),
            text=self.__generate_nickname()
        )
        self.ip_text_box: TextBoxActor = TextBoxActor(
            pygame.Rect(
                settings.SCREEN_WIDTH // 2 - self.TEXT_BOX_WIDTH // 2,
                380,
                self.TEXT_BOX_WIDTH,
                self.TEXT_BOX_HEIGHT
            ),
            text='127.0.0.1:7000'
        )
        self.text_boxes: List[TextBoxActor] = [
            self.nickname_text_box,
            self.ip_text_box
        ]

        self.buttons: List[ButtonActor] = [
            ButtonActor(
                pygame.Rect(
                    settings.SCREEN_WIDTH // 2 - self.TEXT_BOX_WIDTH // 2,
                    480,
                    self.BUTTON_WIDTH,
                    self.BUTTON_HEIGHT
                ),
                text='cancel',
                text_size=20,
                callback=self.back_to_menu
            ),
            ButtonActor(
                pygame.Rect(
                    settings.SCREEN_WIDTH // 2 + (self.TEXT_BOX_WIDTH // 2 - self.BUTTON_WIDTH),
                    480,
                    self.BUTTON_WIDTH,
                    self.BUTTON_HEIGHT
                ),
                text='connect',
                text_size=20,
                callback=self.connect
            )
        ]
    
    def __generate_nickname(self) -> str:
        return 'snake' + str(randint(1000, 9999))

    def connect(self) -> None:
        address: str = self.ip_text_box.text
        if not OnlineSession.is_address_valid(address):
            return
        
        self.online_session.set_address(address)
        print('nickname', self.nickname_text_box.text)
        print('ip', address)
    
    def back_to_menu(self) -> None:
        GameEngine.set_session_forced(menu_scene.MenuScene, menu_viewer.MenuViewer, menu_controller.MenuController)
    
    def update(self, dt: float) -> None:
        pass
