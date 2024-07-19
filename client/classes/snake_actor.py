from game_engine.actor import Actor
from pygame.math import Vector2
from game_engine.direction import Direction
from collections import deque


class SnakeActor(Actor):
    def __init__(self, start_coord: Vector2) -> None:
        super().__init__(start_coord)
        self.direction: Vector2 = Direction.UP
        self.last_move_direction: Vector2 = self.direction.copy()
        self.body: deque[Vector2] = deque([
            self._coord,
            self._coord + Direction.DOWN,
            self._coord + Direction.DOWN * 2
        ])
        self.is_live: bool = True
    
    @property
    def coord(self) -> Vector2:
        if len(self.body) > 0:
            return self.body[0]
        return self._coord
    
    @coord.setter
    def coord(self, new_coord: Vector2) -> None:
        self._coord = new_coord
    
    def move(self) -> None:
        self.body.appendleft(self.body[0] + self.direction)
        self.body.pop()
        self.last_move_direction = self.direction
    
    def set_direction(self, new_direction: Vector2) -> None:
        if new_direction == -self.last_move_direction:
            return
        self.direction = new_direction
    
    def eat(self):
        self.body.append(self.body[-1])
    
    def die(self):
        self.is_live = False
        
