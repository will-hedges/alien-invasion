#!/usr/bin/env python3
# sanic.py - sanic class for blue_sky.py

import pygame


class Sanic:

    def __init__(self, bs_game):
        self.screen = bs_game.screen
        self.screen_rect = bs_game.screen.get_rect()

        self.image = pygame.image.load("images/sanic.png")
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
