from game_engine.game_engine import GameEngine
from scenes.menu_scene import MenuScene
from controllers.menu_controller import MenuController
from viewers.menu_viewer import MenuViewer


if __name__ == '__main__':
    game = GameEngine(MenuViewer, MenuScene, MenuController)
    game.run() # type: ignore
