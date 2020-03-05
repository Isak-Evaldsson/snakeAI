from math import floor
from random import randint
from typing import Tuple
import time
from pygame.locals import *
import pygame

from src.game.player import Player
from src.game.apple import Apple


class Game:
    def isCollision(self, x1, y1, x2, y2, bsize):
        return x1 == x2 and y1 == y2


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
        self.game = Game()
        self.player = Player(self.blockSize)
        self.apple = Apple(5, 5, self.blockSize)

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowSizeX * self.blockSize, self.windowSizeY * self.blockSize), HWSURFACE)

        pygame.display.set_caption(self.caption)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        self.player.update()

        # does snake eat apple?
        for i in range(0, self.player.length):
            if self.game.isCollision(self.apple.x, self.apple.y, self.player.x[i], self.player.y[i], self.blockSize):
                self.apple.x = randint(1, self.windowSizeX)
                self.apple.y = randint(1, self.windowSizeY)
                self.player.grow()

        # does snake collide with itself?
        for i in range(2, self.player.length):
            if self.game.isCollision(self.player.x[0], self.player.y[0], self.player.x[i], self.player.y[i], self.blockSize):
                print("You lose! Collision: ")
                print("x[0] (" + str(self.player.x[0]) + "," + str(self.player.y[0]) + ")")
                print("x[" + str(i) + "] (" + str(self.player.x[i]) + "," + str(self.player.y[i]) + ")")
                exit(0)
        pass

    def on_render(self):
        self._display_surf.fill(self.background_color)
        self.player.draw(self._display_surf)
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
                self.player.move_right()
            elif keys[K_a]:
                self.player.move_left()
            elif keys[K_w]:
                self.player.move_up()
            elif keys[K_s]:
                self.player.move_down()

            time.sleep(50.0 / 1000.0)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == '__main__':
    game = SnakeGame(25, 25)
    game.on_execute()
