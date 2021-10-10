"""Note on a Bar Sprite Manager"""

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
        "rest": 15/15,
        "hold": 14/15,
        "G Low": 13/15,
        "A Low": 12/15,
        "B Low": 11/15,
        "C Low": 10/15,
        "D Low": 9/15,
        "E Low": 8/15,
        "F": 7/15,
        "G High": 6/15,
        "A High": 5/15,
        "B High": 4/15,
        "C High": 3/15,
        "D High": 2/15,
        "E High": 1/15,
        "wild": 0/15,
    })

    def __init__(self, group:pygame.sprite.Group, note:str="rest"):
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
        self.update_note_position()
        group.add(self.note)

    def update_note_position(self):
        self.note.rect.x = self.bar.rect.x + 13
        slider = int(self.bar.rect.height *\
                     self.NOTE_POSITIONS[self.note.note])
        self.note.rect.y = self.bar.rect.y + slider

    def update(self):
        new_note = next(self.note_cycle)
        self.note.update(new_note)
        self.update_note_position()

    def move(self, x:int, y:int):
        self.bar.rect.x = x
        self.bar.rect.y = y
        self.update_note_position()

    def add(self, group: pygame.sprite.Group):
        group.add(self.bar)
        group.add(self.note)

    def remove(self, group: pygame.sprite.Group):
        group.remove(self.bar)
        group.remove(self.note)
