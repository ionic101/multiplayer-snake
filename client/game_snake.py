import pygame
import settings
from model.source.scene import Scene
from model.scenes.menu_scene import MenuScene
from controller.controllers.menu_controller import MenuController, Controller
from view.viewers.menu_viewer import MenuViewer, Viewer


class GameSnake:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption(settings.GAME_NAME)
        
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.game_scene: Scene = MenuScene(self.stop)
        self.game_controller: Controller = MenuController(self.game_scene, stop_game_action=self.stop)
        self.game_viewer: Viewer = MenuViewer(self.screen, self.game_scene)

        self.is_run = False
    

    def update(self) -> None:
        self.game_controller.update()
        self.game_viewer.display()
        pygame.display.flip()
    
    
    def run(self) -> None:
        self.is_run = True
        while self.is_run:
            self.update()
            self.clock.tick(settings.MAX_FPS)
        
        pygame.quit()


    def stop(self) -> None:
        self.is_run = False
