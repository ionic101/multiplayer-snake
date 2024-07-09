from game_engine.actor import Actor
from pygame.math import Vector2
from typing import List
from game_engine.direction import Direction


class SnakeActor(Actor):
    def __init__(self, start_cooord: Vector2) -> None:
        super().__init__(start_cooord)
        self.direction: Vector2 = Direction.UP
        self.body: List[Vector2] = [
            start_cooord,
            start_cooord + Direction.DOWN,
            start_cooord + Direction.DOWN * 2
        ]
    
    def move(self) -> None:
        self.body.insert(0, self.body[0] + self.direction)
        self.body.pop()
    
    def set_direction(self, new_direction: Vector2) -> None:
        self.direction = new_direction
