from typing import Tuple, List
import pygame


# Our snake
class Player:
    x: List[int] = []
    y: List[int] = []
    step: int = 20
    direction: int = 0
    length: int = 3

    color: Tuple[int, int, int] = (0, 255, 0)
    updateCountMax = 2  # Are used to slow down the snake
    updateCount = 0

    def __init__(self, length):
        self.length = length
        for i in range(0, length):
            self.x.append(0)
            self.y.append(0)

    # Handles movement
    def update(self):

        self.updateCount = self.updateCount + 1
        if self.updateCount > self.updateCountMax:

            # update previous positions
            for i in range(self.length - 1, 0, -1):
                self.x[i] = self.x[i - 1]
                self.y[i] = self.y[i - 1]

            # update position of head of snake
            if self.direction == 0:
                self.x[0] += self.step
            if self.direction == 1:
                self.x[0] -= self.step
            if self.direction == 2:
                self.y[0] -= self.step
            if self.direction == 3:
                self.y[0] += self.step

            self.updateCount = 0

    # Sets movement direction
    def move_right(self):
        self.direction = 0

    def move_left(self):
        self.direction = 1

    def move_up(self):
        self.direction = 2

    def move_down(self):
        self.direction = 3

    def grow(self):
        self.length += 1
        self.x.append(self.x[0])
        self.y.append(self.y[0])

    def draw(self, surface):
        for i in range(0, self.length):
            pygame.draw.rect(surface, self.color, [self.x[i], self.y[i], self.step, self.step])
