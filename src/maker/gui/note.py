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

        self.update(note)

    def update(self, note):
        if note not in NOTE_ASSETS:
            raise UnknownNoteSprite(note)

        self.note = note
        self.image = pygame.image.load(NOTE_ASSETS[note])
        self.rect = self.image.get_rect()

