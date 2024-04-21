#!/usr/bin/env python3
#! blue_sky.py - chapter 12 try-it-yourself exercises 12-1 and 12-2

import sys

import pygame

from sanic import Sanic
from settings import Settings


class BlueSky:

    def __init__(self):
        pygame.init()
        self.settings = Settings((1200, 800), (135, 206, 235))

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Blue Sky")

        self.sanic = Sanic(self)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.sanic.blitme()
        pygame.display.flip()

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()


if __name__ == "__main__":
    bs = BlueSky()
    bs.run_game()
