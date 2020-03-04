from typing import Tuple
import pygame


class Apple:
    x = 0
    y = 0
    step = 20
    color: Tuple[int, int, int] = (255, 0, 0)

    def __init__(self, x, y):
        self.x = x * self.step
        self.y = y * self.step

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, [self.x, self.y, self.step, self.step])
