from typing import Tuple, List
from core_game import GameUtils


# Our snake
class BaseSnake:
    x: List[int] = []
    y: List[int] = []
    direction: int = 0
    length: int = 3

    updateCountMax = 2  # Are used to slow down the snake
    updateCount = 0

    def __init__(self):
        for i in range(0, self.length):
            self.x.append(-i)
            self.y.append(-i)

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
                self.x[0] += 1;
            if self.direction == 1:
                self.x[0] -= 1;
            if self.direction == 2:
                self.y[0] -= 1;
            if self.direction == 3:
                self.y[0] += 1;

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
        self.x.append(-self.x[0])
        self.y.append(-self.y[0])

    def tail_collision(self):
        for i in range(2, self.length):
            if GameUtils.isCollision(self.x[0], self.y[0], self.x[i], self.y[i]):
                return True
        else:
            return False

    def wall_collision(self, maxX, maxY):
        return self.x[0] >= maxX or self.x[0] < 0 or self.y[0] >= maxY or self.y[0] < 0
