import pygame
from game_engine.viewer import Viewer
from game_engine.scene import Scene
from game_engine.colors import Colors
from scenes.singleplayer_scene import SingleplayerScene
import game_settings as settings
from viewers.field_viewer import FieldViewer
from viewers.apples_viewer import ApplesViewer
from scenes.singleplayer_scene import GameStatus
from classes.button_actor import ButtonActor


class SingleplayerViewer(Viewer):
    def __init__(self, scene: Scene) -> None:
        super().__init__(scene)
        self._button_font = pygame.font.Font(settings.FONT_PATH, 20)
    
    def __snake_display(self, screen: pygame.Surface) -> None:
        if not isinstance(self._scene, SingleplayerScene):
            return
        
        for cell in self._scene.snake.body:
            pygame.draw.rect(screen,
                             Colors.WHITE,
                             pygame.Rect(cell.x * settings.CELL_WIDTH,
                                        cell.y * settings.CELL_WIDTH,
                                        settings.CELL_WIDTH,
                                        settings.CELL_WIDTH), 3)
    
    def __display_button(self, screen: pygame.Surface, button: ButtonActor) -> None:
        pygame.draw.rect(screen, Colors.WHITE, button.rect, width=5)
        text: pygame.Surface = self._button_font.render(button.text, True, Colors.WHITE)

        text_width: int
        text_height: int
        text_width, text_height = text.get_rect().size

        text_coord = (button.coord.x + (button.width - text_width) // 2,
                      button.coord.y + (button.height - text_height) // 2)
        screen.blit(text, text_coord)

    
    def display(self, screen: pygame.Surface) -> None:
        screen.fill(Colors.BLACK)
        FieldViewer.display(screen)

        if not isinstance(self._scene, SingleplayerScene):
            return

        self.__snake_display(screen)
        ApplesViewer.display(screen, self._scene.apples)

        if self._scene.game_status == GameStatus.PAUSE:
            for button in self._scene.buttons:
                self.__display_button(screen, button)
