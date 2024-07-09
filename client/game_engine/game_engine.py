import pygame
import game_settings as game_settings
from typing import Optional, Type
from game_engine.session import Session
from game_engine.viewer import Viewer
from game_engine.scene import Scene
from game_engine.controller import Controller
from game_engine.base.base_controller import BaseController
from game_engine.base.base_viewer import BaseViewer
from game_engine.base.base_scene import BaseScene


class GameEngine():
    _instance: Optional['GameEngine'] = None
    _initialized: bool = False

    def __new__(cls, *args, **kwargs) -> 'GameEngine': # type: ignore
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, viewer_type: Type[Viewer] = BaseViewer, scene_type: Type[Scene] = BaseScene, controller_type: Type[Controller] = BaseController) -> None:
        if self._initialized:
            return
        pygame.init()
        pygame.display.set_caption(game_settings.GAME_NAME)
        self._screen = pygame.display.set_mode((game_settings.SCREEN_WIDTH, game_settings.SCREEN_HEIGHT))
        self._clock = pygame.time.Clock()
        scene = scene_type()
        viewer = viewer_type(scene)
        controller = controller_type(scene)
        self._session: Session = Session(scene, controller, viewer)
        self.is_run = False
        self._initialized = True
    
    def stop(self) -> None:
        self.is_run = False
    
    def update(self, dt: float) -> None:
        self._session.control(pygame.event.get())
        self._session.update(dt)
        self._session.display(self._screen)
        pygame.display.flip()
    
    def run(self) -> None:
        pygame.init()
        self.is_run = True
        while self.is_run:
            dt: float = self._clock.tick(game_settings.MAX_FPS) / 1000
            self.update(dt)
        pygame.quit()

    def set_session(self, scene_type: Type[Scene] = BaseScene, viewer_type: Type[Viewer] = BaseViewer, controller_type: Type[Controller] = BaseController) -> None:
        self._session.set_scene(scene_type)
        self._session.set_viewer(viewer_type)
        self._session.set_controller(controller_type)
    
    @staticmethod
    def stop_forced() -> None:
        GameEngine().stop()

    @staticmethod
    def set_session_forced(scene_type: Type[Scene] = BaseScene, viewer_type: Type[Viewer] = BaseViewer, controller_type: Type[Controller] = BaseController) -> None:
        GameEngine().set_session(scene_type, viewer_type, controller_type)
