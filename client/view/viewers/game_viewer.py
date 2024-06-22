import pygame
from view.viewer import Viewer
from view.viewers.menu_viewer import MenuViewer
from model.source.game_session_data import GameSessionData
from typing import Union
from model.source.scene import Scene


class GameViewer:
    def __init__(self, screen: pygame.Surface, scene: Scene):
        self._viewer: Viewer = MenuViewer(screen, scene)


    def display(self):
        self._viewer.display()
