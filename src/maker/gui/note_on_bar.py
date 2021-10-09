"""Note on a Bar Sprite"""

__author__="Tyler Westland"

import collections
import itertools
import pygame

from maker.gui.bar import BarSprite
from maker.gui.note import NoteSprite

class UnknownNote(Exception):
    def __init__(self, note: str):
        self.note = note

    def __str__(self) -> str:
        return f"Note on bar is unaware of note: {self.note}"


class NoteOnBar():
    NOTE_POSITIONS = collections.OrderedDict({
        "A": None,
        "B": None
    })

    def __init__(self, group:pygame.sprite.Group, note:str="A"):
        if note not in self.NOTE_POSITIONS:
            raise UnknownNote(note)

        # Infinitely cycle through the notes
        self.note_cycle = itertools.cycle(self.NOTE_POSITIONS)

        # Set cycle to note after given note
        n = next(self.note_cycle)
        while note != n:
            n = next(self.note_cycle)

        # Set up sprites
        self.bar = BarSprite()
        group.add(self.bar)
        self.note = NoteSprite(note)
        group.add(self.note)

    def update(self):
        self.note.update(next(self.note_cycle))

    def add(self, group: pygame.sprite.Group):
        group.add(self.bar)
        group.add(self.note)

    def remove(self, group: pygame.sprite.Group):
        group.remove(self.bar)
        group.remove(self.note)
