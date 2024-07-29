import pygame
from game_engine.viewer import Viewer
from game_engine.scene import Scene
from game_engine.colors import Colors
import scenes.server_searcher_scene as server_searcher_scene
from viewers.button_viewer import ButtonViewer
from viewers.text_box_viewer import TextBoxViewer
import game_settings as settings


class ServerSearcherViewer(Viewer):
    def __init__(self, scene: Scene) -> None:
        super().__init__(scene)
        self._BACKGROUND_COLOR: pygame.Color = Colors.BLACK.value
        self._title_font: pygame.font.Font = pygame.font.Font(settings.FONT_PATH, 30)

        self._FIELD_MARGIN = 35
        self._FIELD_RECT = pygame.Rect(
            self._FIELD_MARGIN,
            self._FIELD_MARGIN,
            settings.SCREEN_WIDTH - self._FIELD_MARGIN * 2,
            settings.SCREEN_HEIGHT - self._FIELD_MARGIN * 2
        )

    def __display_ip(self, screen: pygame.Surface) -> None:
        rendered_text: pygame.Surface = self._title_font.render('IP', True, Colors.WHITE.value)
        text_width: int = rendered_text.get_rect().width
        text_coord = (settings.SCREEN_WIDTH // 2 - text_width // 2, 335)
        screen.blit(rendered_text, text_coord)
    
    def __display_nickname(self, screen: pygame.Surface) -> None:
        rendered_text: pygame.Surface = self._title_font.render('NICKNAME', True, Colors.WHITE.value)
        text_width: int = rendered_text.get_rect().width
        text_coord = (settings.SCREEN_WIDTH // 2 - text_width // 2, 190)
        screen.blit(rendered_text, text_coord)
    
    def __display_field(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen,
                         Colors.WHITE.value,
                         self._FIELD_RECT,
                         width=5)
    
    def display(self, screen: pygame.Surface) -> None:
        screen.fill(self._BACKGROUND_COLOR)
        self.__display_field(screen)

        if not isinstance(self._scene, server_searcher_scene.ServerSearcherScene):
            return
        
        if not self._scene.is_connecting:
            self.__display_ip(screen)
            self.__display_nickname(screen)
            
            for text_box in self._scene.text_boxes:
                TextBoxViewer.display(screen, text_box)

            for button in self._scene.buttons:
                ButtonViewer.display(screen, button)
        
        