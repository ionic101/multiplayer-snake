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
import os
import pickle


class GameStatus:
    START = 0
    PLAY = 1
    PAUSE = 2
    END = 3


class SingleplayerScene(Scene):
    def __init__(self) -> None:
        self.snake: SnakeActor = SnakeActor(Vector2(20, 20))
        self.apples: List[Vector2] = []
        self.move_time: float = 0.0
        self.record: int = len(self.snake.body)
        self.COUNT_APPLES: int = 5
        self.MOVE_TIME: float = 0.2
        self.FIELD_START_COORD: Vector2 = Vector2(2, 2)
        self.FIELD_END_COORD: Vector2 = Vector2(61, 29)
        self.__game_status: int = GameStatus.START
        self.init_apples()

        self._BUTTON_WIDTH: int = 300
        self._BUTTON_HEIGHT: int = 70
        self._BUTTOM_INTERVAL: int = 100

        self.buttons: List[ButtonActor] = []
        self._PAUSE_BUTTONS: List[ButtonActor] = [
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
        self._END_BUTTONS: List[ButtonActor] = [
            ButtonActor(
                rect=pygame.Rect(
                    settings.SCREEN_WIDTH // 2 - self._BUTTON_WIDTH // 2,
                    settings.SCREEN_HEIGHT // 2 - self._BUTTON_HEIGHT // 2,
                    self._BUTTON_WIDTH,
                    self._BUTTON_HEIGHT
                ),
                text='restart',
                callback=self.restart_game
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
    
    @property
    def game_status(self) -> int:
        return self.__game_status
    
    @game_status.setter
    def game_status(self, new_game_status: int) -> None:
        if new_game_status == GameStatus.PLAY or new_game_status == GameStatus.START:
            self.buttons = []
        elif new_game_status == GameStatus.PAUSE:
            self.buttons = self._PAUSE_BUTTONS
        elif new_game_status == GameStatus.END:
            self.buttons = self._END_BUTTONS

        self.__game_status = new_game_status
    
    @property
    def score(self) -> int:
        return len(self.snake.body)
    
    def continue_game(self) -> None:
        self.game_status = GameStatus.PLAY
    
    def restart_game(self) -> None:
        self.__init__()
    
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
        new_snake_coord: Vector2 = self.snake.coord + self.snake.direction.value
        
        if new_snake_coord in self.snake.body or new_snake_coord.x < self.FIELD_START_COORD.x\
            or new_snake_coord.x > self.FIELD_END_COORD.x or new_snake_coord.y < self.FIELD_START_COORD.y\
            or new_snake_coord.y > self.FIELD_END_COORD.y:
            self.stop()
            return
        
        self.check_shake_on_apple(new_snake_coord)
        self.snake.move()
    
    def start(self) -> None:
        if os.path.exists(settings.RECORD_PATH):
            with open(settings.RECORD_PATH, 'rb') as file:
                self.record = pickle.load(file)
        self.game_status = GameStatus.PLAY
    
    def play(self, dt: float) -> None:
        self.move_time += dt
        if self.snake.is_live and self.move_time >= self.MOVE_TIME:
            self.update_snake()
            self.move_time = 0.0
    
    def pause(self) -> None:
        pass

    def stop(self) -> None:
        self.snake.die()
        self.game_status = GameStatus.END
        self.record = max(self.score, self.record)

        data_dir = os.path.dirname(settings.RECORD_PATH)
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        
        with open(settings.RECORD_PATH, 'wb') as file:
            pickle.dump(self.record, file)
    
    def update(self, dt: float) -> None:
        match self.game_status:
            case GameStatus.START:
                self.start()
            case GameStatus.PLAY:
                self.play(dt)
            case GameStatus.PAUSE:
                self.pause()
            case GameStatus.END:
                pass
            case _:
                pass
