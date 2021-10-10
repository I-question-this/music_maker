"""Bar Sprite"""

__author__="Tyler Westland"

import pygame

from maker.gui.assets import BAR_ASSET

class BarSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load(BAR_ASSET)
        self.image = pygame.transform.scale(
                self.image, (90, 140))
        self.rect = self.image.get_rect()
