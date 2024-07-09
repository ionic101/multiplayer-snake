import pygame
from game_engine.colors import Colors
import game_settings


class FieldViewer:
    FIELD_MARGIN = 35
    FIELD_RECT = pygame.Rect(
            FIELD_MARGIN,
            FIELD_MARGIN,
            game_settings.SCREEN_WIDTH - FIELD_MARGIN * 2,
            game_settings.SCREEN_HEIGHT - FIELD_MARGIN * 2
        )

    @staticmethod
    def display(screen: pygame.Surface) -> None:
        pygame.draw.rect(screen,
                         Colors.WHITE,
                         FieldViewer.FIELD_RECT,
                         width=5)
