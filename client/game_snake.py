import pygame
import settings
from view.game_viewer import GameViewer


class GameSnake:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption(settings.GAME_NAME)
        
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.gameViewer = GameViewer(self.screen)

        self.is_run = False
    

    def update(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_run = False

        self.gameViewer.display()
        
    
    
    def run(self) -> None:
        self.is_run = True
        while self.is_run:
            self.update()
            self.clock.tick(settings.MAX_FPS)
        
        pygame.quit()
