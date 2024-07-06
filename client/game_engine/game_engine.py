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


    def __new__(cls, *args, **kwargs) -> Optional['GameEngine']: # type: ignore
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


    def __init__(self, viewer_type: Type[Viewer] = BaseViewer, scene_type: Type[Scene] = BaseScene, controller_type: Type[Controller] = BaseController) -> None:
        pygame.init()
        pygame.display.set_caption(game_settings.GAME_NAME)
        self._screen = pygame.display.set_mode((game_settings.SCREEN_WIDTH, game_settings.SCREEN_HEIGHT))
        self._clock = pygame.time.Clock()

        scene = scene_type()
        viewer = viewer_type(self._screen, scene)
        controller = controller_type(scene)

        self._session: Session = Session(scene, controller, viewer)
        self.is_run = False
    

    def stop(self) -> None:
        self.is_run = False
    
    
    def update(self) -> None:
        self._session.control()
        self._session.display()
        pygame.display.flip()
    
    
    def run(self) -> None:
        pygame.init()
        self.is_run = True
        while self.is_run:
            self.update()
            self._clock.tick(game_settings.MAX_FPS)
        pygame.quit()


    @staticmethod
    def quit() -> None:
        GameEngine().stop() # type: ignore
