import pygame
from view.viewer import Viewer
from model.source.game_session_data import GameSessionData
from model.source.scene import Scene
from model.scenes.menu_scene import MenuScene


class MenuViewer(Viewer):
    def __init__(self, screen: pygame.Surface, scene: Scene) -> None:
        super().__init__(screen, scene)
        self._BACKGROUND_COLOR: pygame.Color = pygame.Color(0, 0, 0)
    
    
    def display(self) -> None:
        self._screen.fill(self._BACKGROUND_COLOR)

        if not isinstance(self._scene, MenuScene):
            return

        for button in self._scene.buttons:
            pygame.draw.rect(self._screen, button.color, button.rect)
