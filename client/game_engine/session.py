from game_engine.scene import Scene
from game_engine.controller import Controller
from game_engine.viewer import Viewer
from typing import Type, List
import pygame


class Session():
    def __init__(self, scene: Scene, controller: Controller, viewer: Viewer) -> None:
        self._scene: Scene = scene
        self._controller: Controller = controller
        self._viewer: Viewer = viewer
    
    def update(self, dt: float) -> None:
        self._scene.update(dt)

    def display(self, screen: pygame.Surface) -> None:
        self._viewer.display(screen)

    def control(self, events: List[pygame.event.Event]) -> None:
        self._controller.control(events)

    def set_viewer(self, viewer_type: Type[Viewer]):
        assert issubclass(viewer_type, Viewer), Exception('In argument must be type of viewer')
        self._viewer = viewer_type(self._scene)

    def set_controller(self, controller_type: Type[Controller]):
        assert issubclass(controller_type, Controller), Exception('In argument must be type of controller')
        self._controller = controller_type(self._scene)

    def set_scene(self, scene_type: Type[Scene]):
        assert issubclass(scene_type, Scene), Exception('In argument must be type of scene')
        self._scene = scene_type()
        self._viewer.set_scene(self._scene)
        self._controller.set_scene(self._scene)
