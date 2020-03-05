from math import floor
from random import randint
from typing import Tuple
import time
from pygame.locals import *
import pygame

from src.game.snake import Snake
from src.game.apple import Apple
from src.game.gameUtils import GameUtils


class SnakeGame:
    blockSize = 20

    def __init__(self, windowSizeX: int, windowSizeY: int, caption: str = "SnakeGame",
                 background_color: Tuple[int, int, int] = (0, 0, 0)):
        self.windowSizeX = windowSizeX
        self.windowSizeY = windowSizeY
        self.caption = caption
        self.background_color = background_color

        # State variables
        self._running = False
        self._display_surf = None
        self.snake = Snake(self.blockSize)
        self.apple = Apple(5, 5, self.blockSize)

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(
            (self.windowSizeX * self.blockSize, self.windowSizeY * self.blockSize), HWSURFACE)

        pygame.display.set_caption(self.caption)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        self.snake.update()
        self.on_collision()
        pass

    def on_collision(self):
        self.apple.snakeCollision(self.snake, self.windowSizeX, self.windowSizeY)

        if self.snake.tailCollision() or self.snake.wallCollison(self.windowSizeX, self.windowSizeY):
            print("You lost the game")
            exit(0)

    def on_render(self):
        self._display_surf.fill(self.background_color)
        self.snake.draw(self._display_surf)
        self.apple.draw(self._display_surf)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        self.on_init()

        while self._running:
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if keys[K_ESCAPE]:
                self._running = False
            elif keys[K_d]:
                self.snake.move_right()
            elif keys[K_a]:
                self.snake.move_left()
            elif keys[K_w]:
                self.snake.move_up()
            elif keys[K_s]:
                self.snake.move_down()

            time.sleep(50.0 / 1000.0)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == '__main__':
    game = SnakeGame(25, 25)
    game.on_execute()
