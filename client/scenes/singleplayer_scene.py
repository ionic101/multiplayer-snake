from game_engine.scene import Scene
import game_settings as settings
from classes.snake_actor import SnakeActor
from pygame.math import Vector2
from typing import List
from random import choice
from classes.button_actor import ButtonActor
import pygame
from game_engine.game_engine import GameEngine
import scenes.menu_scene as menu_scene
import viewers.menu_viewer as menu_viewer
import controllers.menu_controller as menu_controller


class GameStatus:
    PLAY = 0
    PAUSE = 1
    END = 2


class SingleplayerScene(Scene):
    def __init__(self) -> None:
        self.snake: SnakeActor = SnakeActor(Vector2(20, 20))
        self.apples: List[Vector2] = []
        self.move_time: float = 0.0
        self.COUNT_APPLES: int = 5
        self.MOVE_TIME: float = 0.2
        self.FIELD_START_COORD: Vector2 = Vector2(2, 2)
        self.FIELD_END_COORD: Vector2 = Vector2(settings.SCREEN_WIDTH // settings.CELL_WIDTH - 3, settings.SCREEN_HEIGHT // settings.CELL_WIDTH - 3)
        self.game_status: int = GameStatus.PLAY
        self.init_apples()

        self._BUTTON_WIDTH: int = 300
        self._BUTTON_HEIGHT: int = 70
        self._BUTTOM_INTERVAL: int = 100

        self.buttons: List[ButtonActor] = [
            ButtonActor(
                rect=pygame.Rect(
                    settings.SCREEN_WIDTH // 2 - self._BUTTON_WIDTH // 2,
                    settings.SCREEN_HEIGHT // 2 - self._BUTTON_HEIGHT // 2,
                    self._BUTTON_WIDTH,
                    self._BUTTON_HEIGHT
                ),
                text='continue',
                callback=self.continue_game
            ),
            ButtonActor(
                rect=pygame.Rect(
                    settings.SCREEN_WIDTH // 2 - self._BUTTON_WIDTH // 2,
                    settings.SCREEN_HEIGHT // 2 - self._BUTTON_HEIGHT // 2 + self._BUTTOM_INTERVAL,
                    self._BUTTON_WIDTH,
                    self._BUTTON_HEIGHT
                ),
                text='quit',
                callback=self.quit
            ),
        ]
    
    def continue_game(self) -> None:
        self.game_status = GameStatus.PLAY
    
    def quit(self) -> None:
        GameEngine.set_session_forced(menu_scene.MenuScene, menu_viewer.MenuViewer, menu_controller.MenuController)
    
    def init_apples(self):
        for _ in range(self.COUNT_APPLES):
            self.spawn_apple()
    
    def spawn_apple(self) -> None:
        apple_spawn_coords: List[Vector2] = []
        for x in range(int(self.FIELD_START_COORD.x), int(self.FIELD_END_COORD.x) + 1):
            for y in range(int(self.FIELD_START_COORD.y), int(self.FIELD_END_COORD.y) + 1):
                apple_coord: Vector2 = Vector2(x, y)
                if apple_coord not in self.apples and apple_coord not in self.snake.body:
                    apple_spawn_coords.append(apple_coord)

        self.apples.append(choice(apple_spawn_coords))

    def check_shake_on_apple(self, snake_coord: Vector2) -> None:
        for ind, apple_coord in enumerate(self.apples):
            if apple_coord == snake_coord:
                self.snake.eat()
                self.apples.pop(ind)
                self.spawn_apple()
    
    def update_snake(self) -> None:
        new_snake_coord: Vector2 = self.snake.coord + self.snake.direction
        
        if new_snake_coord in self.snake.body or new_snake_coord.x < self.FIELD_START_COORD.x\
            or new_snake_coord.x > self.FIELD_END_COORD.x or new_snake_coord.y < self.FIELD_START_COORD.y\
            or new_snake_coord.y > self.FIELD_END_COORD.y:
            self.snake.die()
            return
        
        self.check_shake_on_apple(new_snake_coord)
        self.snake.move()
    
    def play(self, dt: float) -> None:
        self.move_time += dt
        if self.snake.is_live and self.move_time >= self.MOVE_TIME:
            self.update_snake()
            self.move_time = 0.0
    
    def pause(self) -> None:
        pass

    def end(self) -> None:
        pass
    
    def update(self, dt: float) -> None:
        match self.game_status:
            case GameStatus.PLAY:
                self.play(dt)
            case GameStatus.PAUSE:
                pass
            case GameStatus.END:
                pass
            case _:
                pass
