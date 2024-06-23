from client.model.classes.snake_actor import SnakeActor
from controller.controller import Controller


class SnakeController(Controller):
    def __init__(self, snake: SnakeActor) -> None:
        self.snake = snake
