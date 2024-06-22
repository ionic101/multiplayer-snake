from model.scenes.menu_scene import MenuScene, Scene


class GameSessionData:
    def __init__(self) -> None:
        self._scene: Scene = MenuScene()