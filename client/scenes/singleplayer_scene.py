from game_engine.scene import Scene
import game_settings as game_settings
from classes.snake_actor import SnakeActor
from pygame.math import Vector2


class SingleplayerScene(Scene):
    def __init__(self) -> None:
        self.snake: SnakeActor = SnakeActor(Vector2(5, 5))
        self.move_time: float = 0.0
    
    def update(self, dt: float) -> None:
        self.move_time += dt
        if self.move_time >= 0.5:
            self.snake.move()
            self.move_time = 0.0
