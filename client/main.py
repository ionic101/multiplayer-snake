from game_engine.game_engine import GameEngine
from scenes.menu_scene import MenuScene
from controllers.menu_controller import MenuController
from viewers.menu_viewer import MenuViewer
import pygame
import game_settings as settings


if __name__ == '__main__':
    game = GameEngine(MenuViewer, MenuScene, MenuController)
    pygame.display.set_icon(pygame.image.load(settings.ICON_PATH))
    game.run()
