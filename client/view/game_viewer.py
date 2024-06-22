import pygame


class GameViewer:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen

    def display(self):
        self.screen.fill((200, 0, 0))
        pygame.display.flip()
