import pygame
from game_engine.viewer import Viewer
from game_engine.scene import Scene
from scenes.menu_scene import MenuScene
from game_engine.colors import Colors
import game_settings as game_settings
from classes.button_actor import ButtonActor


class MenuViewer(Viewer):
    def __init__(self, screen: pygame.Surface, scene: Scene) -> None:
        super().__init__(screen, scene)
        self._BACKGROUND_COLOR: pygame.Color = Colors.BLACK
        self._button_font = pygame.font.Font(game_settings.FONT_PATH, 20)
        self._title_font = pygame.font.Font(game_settings.FONT_PATH, 60)

        self._FIELD_MARGIN = 30
        self._FIELD_RECT = pygame.Rect(
            self._FIELD_MARGIN,
            self._FIELD_MARGIN,
            game_settings.SCREEN_WIDTH - self._FIELD_MARGIN * 2,
            game_settings.SCREEN_HEIGHT - self._FIELD_MARGIN * 2
        )


    def __display_field(self) -> None:
        pygame.draw.rect(self._screen,
                         Colors.WHITE,
                         self._FIELD_RECT,
                         width=5)
    

    def __display_title(self) -> None:
        title: pygame.Surface = self._title_font.render(game_settings.GAME_NAME, True, Colors.WHITE)

        title_width: int
        title_height: int
        title_width, title_height = title.get_rect().size

        title_coord = (game_settings.SCREEN_WIDTH // 2 - title_width // 2, game_settings.SCREEN_HEIGHT // 4 - title_height // 2)

        self._screen.blit(title, title_coord)
    


    def __display_button(self, button: ButtonActor) -> None:
        pygame.draw.rect(self._screen, Colors.WHITE, button.rect, width=5)
        text: pygame.Surface = self._button_font.render(button.text, True, Colors.WHITE)

        text_width: int
        text_height: int
        text_width, text_height = text.get_rect().size

        text_coord = (button.coord.x + (button.width - text_width) // 2,
                      button.coord.y + (button.height - text_height) // 2)
        self._screen.blit(text, text_coord)
    

    def display(self) -> None:
        self._screen.fill(self._BACKGROUND_COLOR)
        self.__display_field()
        self.__display_title()

        if not isinstance(self._scene, MenuScene):
            return

        for button in self._scene.buttons:
            self.__display_button(button)
