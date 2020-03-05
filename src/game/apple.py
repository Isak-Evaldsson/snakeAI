from random import randint
from typing import Tuple
import pygame

from src.game.snake import Snake


class Apple:
    x = 0
    y = 0
    color: Tuple[int, int, int] = (255, 0, 0)

    def __init__(self, x, y, blockSize):
        self.blockSize = blockSize
        self.x = x
        self.y = y

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, [self.x*self.blockSize, self.y*self.blockSize, self.blockSize, self.blockSize])

    def snakeCollision(self, snake: Snake, maxX, maxY):
        if snake.x[0] == self.x and snake.y[0] == self.y:
            snake.grow()
            self.x = randint(0, maxX)
            self.y = randint(0, maxY)