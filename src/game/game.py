from typing import Tuple
import time
from pygame.locals import *
import pygame

from src.game.player import Player


class SnakeGame:
    def __init__(self, window_width: int = 500, window_height: int = 500, caption: str = "SnakeGame",
                 background_color: Tuple[int, int, int] = (0, 0, 0)):
        self.window_width = window_width
        self.window_height = window_height
        self.caption = caption
        self.background_color = background_color

        # State variables
        self._running = False
        self._display_surf = None
        self.player = Player(10)

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.window_width, self.window_height), HWSURFACE)

        pygame.display.set_caption(self.caption)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        self.player.update()
        pass

    def on_render(self):
        self._display_surf.fill(self.background_color)
        self.player.draw(self._display_surf)
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
            elif keys[K_RIGHT]:
                self.player.move_right()
            elif keys[K_LEFT]:
                self.player.move_left()
            elif keys[K_UP]:
                self.player.move_up()
            elif keys[K_DOWN]:
                self.player.move_down()

            time.sleep(50.0 / 1000.0)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == '__main__':
    game = SnakeGame()
    game.on_execute()
