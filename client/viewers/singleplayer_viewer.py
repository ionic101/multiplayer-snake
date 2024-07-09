import pygame
from game_engine.viewer import Viewer
from game_engine.scene import Scene
from game_engine.colors import Colors
from scenes.singleplayer_scene import SingleplayerScene
import game_settings as settings


class SingleplayerViewer(Viewer):
    def __init__(self, scene: Scene) -> None:
        super().__init__(scene)
    
    def __snake_display(self, screen: pygame.Surface) -> None:
        if not isinstance(self._scene, SingleplayerScene):
            return
        
        for cell in self._scene.snake.body:
            pygame.draw.rect(screen,
                             Colors.RED,
                             pygame.Rect(cell.x * settings.CELL_WIDTH,
                                        cell.y * settings.CELL_WIDTH,
                                        settings.CELL_WIDTH,
                                        settings.CELL_WIDTH), 3)
    
    def display(self, screen: pygame.Surface) -> None:
        screen.fill(Colors.BLACK)
        self.__snake_display(screen)
