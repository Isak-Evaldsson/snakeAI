from typing import Tuple
from core_game import BaseApple
import pygame


class Apple(BaseApple):
    x = 0
    y = 0

    color: Tuple[int, int, int] = (255, 0, 0)

    def __init__(self, x, y, block_size):
        BaseApple.__init__(self, x, y)
        self.block_size = block_size

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, [self.x*self.block_size, self.y*self.block_size, self.block_size, self.block_size])
