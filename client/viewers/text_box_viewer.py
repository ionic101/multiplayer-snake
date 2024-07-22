import pygame
from game_engine.colors import Colors
import game_settings as settings
from classes.text_box_actor import TextBoxActor


class TextBoxViewer:
    @staticmethod
    def display(screen: pygame.Surface, button: TextBoxActor) -> None:
        pygame.draw.rect(screen, Colors.WHITE.value, button.rect, width=5)
        text: pygame.Surface = pygame.font.Font(settings.FONT_PATH, button.text_size)\
            .render(button.text, True, Colors.WHITE.value)

        text_width: int
        text_height: int
        text_width, text_height = text.get_rect().size

        text_coord = (button.coord.x + (button.width - text_width) // 2,
                      button.coord.y + (button.height - text_height) // 2)
        screen.blit(text, text_coord)
