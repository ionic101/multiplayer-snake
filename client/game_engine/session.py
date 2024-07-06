from game_engine.scene import Scene
from game_engine.controller import Controller
from game_engine.viewer import Viewer


class Session():
    def __init__(self, scene: Scene, controller: Controller, viewer: Viewer) -> None:
        self._scene: Scene = scene
        self._controller: Controller = controller
        self._viewer: Viewer = viewer


    def display(self):
        self._viewer.display()


    def control(self):
        self._controller.control()
    

    def set_viewer(self, new_viewer: Viewer):
        assert isinstance(new_viewer, Viewer), Exception('In agument must be viewer')
        self._viewer = new_viewer
    

    def set_controller(self, new_controller: Controller):
        assert isinstance(new_controller, Controller), Exception('In agument must be controller')
        self._controller = new_controller
