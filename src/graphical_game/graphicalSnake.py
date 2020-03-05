from typing import Tuple, List
from core_game import BaseSnake, GameUtils
import pygame


# Our snake
class GraphicalSnake(BaseSnake):
    blockSize: int = 20
    color: Tuple[int, int, int] = (0, 255, 0)

    def __init__(self, blockSize):
        BaseSnake.__init__(self)
        self.blockSize = blockSize

    def draw(self, surface):
        for i in range(0, self.length):
            pygame.draw.rect(surface, self.color,
                             [self.x[i] * self.blockSize, self.y[i] * self.blockSize, self.blockSize, self.blockSize])
