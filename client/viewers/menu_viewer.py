import pygame
from game_engine.viewer import Viewer
from game_engine.scene import Scene
import scenes.menu_scene as menu_scene
from game_engine.colors import Colors
import game_settings as settings
from viewers.button_viewer import ButtonViewer


class MenuViewer(Viewer):
    def __init__(self, scene: Scene) -> None:
        super().__init__(scene)
        self._BACKGROUND_COLOR: pygame.Color = Colors.BLACK.value
        self._title_font = pygame.font.Font(settings.FONT_PATH, 100)

        self._FIELD_MARGIN = 35
        self._FIELD_RECT = pygame.Rect(
            self._FIELD_MARGIN,
            self._FIELD_MARGIN,
            settings.SCREEN_WIDTH - self._FIELD_MARGIN * 2,
            settings.SCREEN_HEIGHT - self._FIELD_MARGIN * 2
        )
    
    def __display_field(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen,
                         Colors.WHITE.value,
                         self._FIELD_RECT,
                         width=5)

    def __display_title(self, screen: pygame.Surface) -> None:
        title: pygame.Surface = self._title_font.render(settings.GAME_NAME, True, Colors.WHITE.value)

        title_width: int
        title_height: int
        title_width, title_height = title.get_rect().size

        title_coord = (settings.SCREEN_WIDTH // 2 - title_width // 2, settings.SCREEN_HEIGHT // 4 - title_height // 2)

        screen.blit(title, title_coord)
    
    def display(self, screen: pygame.Surface) -> None:
        screen.fill(self._BACKGROUND_COLOR)
        self.__display_field(screen)
        self.__display_title(screen)

        if not isinstance(self._scene, menu_scene.MenuScene):
            return

        for button in self._scene.buttons:
            ButtonViewer.display(screen, button)
