from game_engine.scene import Scene
from classes.text_box_actor import TextBoxActor
from classes.button_actor import ButtonActor
import pygame
import game_settings as settings
from random import randint
from typing import List, Dict, Any, Optional
import scenes.menu_scene as menu_scene
import viewers.menu_viewer as menu_viewer
import controllers.menu_controller as menu_controller
from game_engine.game_engine import GameEngine
from game_engine.online_session import OnlineSession
from scenes.multiplayer_scene import MultiplayerScene
from viewers.multiplayer_viewer import MultiplayerViewer
from controllers.multiplayer_controller import MultiplayerController


class ServerSearcherScene(Scene):
    def __init__(self) -> None:
        super().__init__()

        self.online_session: OnlineSession = OnlineSession()
        self.is_connecting: bool = False

        self.TEXT_BOX_WIDTH: int = 500
        self.TEXT_BOX_HEIGHT: int = 70
        self.DEFAULT_BUTTON_WIDTH: int = 210
        self.DEFAULT_BUTTON_HEIGHT: int = 70
        self._CANCEL_CONNECT_WIDTH: int = 250
        self._CANCEL_CONNECT_HEIGTH: int = 70

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

        self._BACK_TO_MENU_BUTTON: ButtonActor = ButtonActor(
            pygame.Rect(
                settings.SCREEN_WIDTH // 2 - self.TEXT_BOX_WIDTH // 2,
                480,
                self.DEFAULT_BUTTON_WIDTH,
                self.DEFAULT_BUTTON_HEIGHT
            ),
            text='cancel',
            text_size=20,
            callback=self.back_to_menu
        )
        self._CONNECT_BUTTON: ButtonActor = ButtonActor(
            pygame.Rect(
                settings.SCREEN_WIDTH // 2 + (self.TEXT_BOX_WIDTH // 2 - self.DEFAULT_BUTTON_WIDTH),
                480,
                self.DEFAULT_BUTTON_WIDTH,
                self.DEFAULT_BUTTON_HEIGHT
            ),
            text='connect',
            text_size=20,
            callback=self.connect
        )
        self._CANCEL_CONNECT_BUTTON: ButtonActor = ButtonActor(
            pygame.Rect(
                    settings.SCREEN_WIDTH // 2 - self._CANCEL_CONNECT_WIDTH // 2,
                    400,
                    self._CANCEL_CONNECT_WIDTH,
                    self._CANCEL_CONNECT_HEIGTH
                ),
                text='cancel',
                text_size=20,
                callback=self.cancel_connect
        )
        self.buttons: List[ButtonActor] = [self._BACK_TO_MENU_BUTTON, self._CONNECT_BUTTON]
    
    def __generate_nickname(self) -> str:
        return 'snake' + str(randint(1000, 9999))
    
    def cancel_connect(self) -> None:
        self.buttons = [self._BACK_TO_MENU_BUTTON, self._CONNECT_BUTTON]
        self.is_connecting = False

    def connect(self) -> None:
        nickname: str = self.nickname_text_box.text
        address: str = self.ip_text_box.text
        if not OnlineSession.is_address_valid(address):
            print('Invalid address')
            return
        
        self.online_session.set_address(address)
        self.online_session.send({
            'type': 'connect',
            'nickname': nickname
        })
        self.buttons = [self._CANCEL_CONNECT_BUTTON]
        self.is_connecting = True
    
    def back_to_menu(self) -> None:
        GameEngine.set_session_forced(menu_scene.MenuScene, menu_viewer.MenuViewer, menu_controller.MenuController)
    
    def start_game(self) -> None:
        GameEngine.set_session_forced(MultiplayerScene, MultiplayerViewer, MultiplayerController)
        
    def update(self, dt: float) -> None:
        if not self.is_connecting:
            return
        
        data: Optional[Dict[str, Any]] = self.online_session.get()
        if data is not None and data.get('type') == 'connect' and data.get('status'):
            self.start_game()
        