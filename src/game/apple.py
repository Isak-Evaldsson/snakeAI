from typing import Tuple
import pygame


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
