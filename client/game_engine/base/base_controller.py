from game_engine.controller import Controller
from game_engine.scene import Scene



class BaseController(Controller):
    def __init__(self, scene: Scene) -> None:
        super().__init__(scene)
    

    def control(self) -> None:
        super().control()
