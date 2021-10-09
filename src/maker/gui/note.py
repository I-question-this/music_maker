"""Note sprite"""

__author__="Tyler Westland"

import pygame

from maker.gui.assets import NOTE_ASSETS

class UnknownNoteSprite(Exception):
    def __init__(self, note: str):
        self.note = note

    def __str__(self) -> str:
        return f"No sprite for note: {self.note}"


class NoteSprite(pygame.sprite.Sprite):
    def __init__(self, note:str):
        super().__init__()

        if note not in NOTE_ASSETS:
            raise UnknownNoteSprite(note)

        self.image = pygame.image.load(NOTE_ASSETS[note])
        self.rect = self.image.get_rect()

    def update(self, note:str="A"):
        self.image = pygame.image.load(NOTE_ASSETS[note])
        self.rect = self.image.get_rect()

