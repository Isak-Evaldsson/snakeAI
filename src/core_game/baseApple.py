from random import randint
from typing import Tuple
from core_game import BaseSnake


class BaseApple:
    x = 0
    y = 0
    color: Tuple[int, int, int] = (255, 0, 0)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def snake_collision(self, snake: BaseSnake, maxX, maxY):
        if snake.x[0] == self.x and snake.y[0] == self.y:
            snake.grow()
            self.x = randint(0, maxX)
            self.y = randint(0, maxY)
