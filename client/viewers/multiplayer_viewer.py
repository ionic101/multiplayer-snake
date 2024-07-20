import pygame
from game_engine.viewer import Viewer
from game_engine.scene import Scene
from game_engine.colors import Colors
from scenes.multiplayer_scene import MultiplayerScene, GameStatus
import game_settings as settings
from viewers.apples_viewer import ApplesViewer
from classes.button_actor import ButtonActor


class MultiplayerViewer(Viewer):
    def __init__(self, scene: Scene) -> None:
        super().__init__(scene)
        self._button_font: pygame.font.Font = pygame.font.Font(settings.FONT_PATH, 20)
        self._status_font: pygame.font.Font = pygame.font.Font(settings.FONT_PATH, 30)
        self._title_font: pygame.font.Font = pygame.font.Font(settings.FONT_PATH, 50)

        self._STATUS_RIGHT_MARGIN: int = 100
        self._STATUS_LEFT_MARGIN: int = 225 + self._STATUS_RIGHT_MARGIN
        self._FIELD_MARGIN = 35
        self._FIELD_RECT = pygame.Rect(
                self._FIELD_MARGIN,
                self._FIELD_MARGIN,
                settings.SCREEN_WIDTH - self._FIELD_MARGIN * 2,
                settings.SCREEN_HEIGHT - settings.CELL_WIDTH * 4 - self._FIELD_MARGIN * 2
            )
    
    def __display_field(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen,
                         Colors.WHITE.value,
                         self._FIELD_RECT,
                         width=5)
    
    def __display_snake(self, screen: pygame.Surface) -> None:
        if not isinstance(self._scene, MultiplayerScene):
            return
        
        for cell in self._scene.snake.body:
            pygame.draw.rect(screen,
                             Colors.WHITE.value,
                             pygame.Rect(cell.x * settings.CELL_WIDTH,
                                        cell.y * settings.CELL_WIDTH,
                                        settings.CELL_WIDTH,
                                        settings.CELL_WIDTH))
    
    def __display_button(self, screen: pygame.Surface, button: ButtonActor) -> None:
        pygame.draw.rect(screen, Colors.WHITE.value, button.rect, width=5)
        text: pygame.Surface = self._button_font.render(button.text, True, Colors.WHITE.value)
        text_width: int
        text_height: int
        text_width, text_height = text.get_rect().size
        text_coord = (button.coord.x + (button.width - text_width) // 2,
                      button.coord.y + (button.height - text_height) // 2)
        screen.blit(text, text_coord)
    
    def __display_score(self, screen: pygame.Surface) -> None:
        if not isinstance(self._scene, MultiplayerScene):
            return
        score: pygame.Surface = self._status_font.render(f'score {self._scene.score}', True, Colors.WHITE.value)
        score_coord = (settings.SCREEN_WIDTH // 2 - self._STATUS_LEFT_MARGIN, 640)
        screen.blit(score, score_coord)
    
    def __display_record(self, screen: pygame.Surface) -> None:
        if not isinstance(self._scene, MultiplayerScene):
            return
        score: pygame.Surface = self._status_font.render(f'record {self._scene.record}', True, Colors.WHITE.value)
        score_coord = (settings.SCREEN_WIDTH // 2 + self._STATUS_RIGHT_MARGIN, 640)
        screen.blit(score, score_coord)
    
    def __display_title(self, screen: pygame.Surface, text: str) -> None:
        rendered_text: pygame.Surface = self._title_font.render(text, True, Colors.WHITE.value)
        text_width: int = rendered_text.get_rect().width
        text_coord = (settings.SCREEN_WIDTH // 2 - text_width // 2, 200)
        screen.blit(rendered_text, text_coord)
    
    def display(self, screen: pygame.Surface) -> None:
        screen.fill(Colors.BLACK.value)
        self.__display_field(screen)

        if not isinstance(self._scene, MultiplayerScene):
            return
        
        self.__display_score(screen)
        self.__display_record(screen)
        self.__display_snake(screen)
        ApplesViewer.display(screen, self._scene.apples)

        for button in self._scene.buttons:
            self.__display_button(screen, button)

        if self._scene.game_status == GameStatus.END:
            self.__display_title(screen, 'GAME OVER')
        elif self._scene.game_status == GameStatus.PAUSE:
            self.__display_title(screen, 'PAUSE')
