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
        "rest": 1,
        "hold": 0.9,
        "G Low": 0.8,
        "A Low": 0.7,
        "B Low": 0.6,
        "C Low": 0.5,
        "D Low": 0.4,
        "E Low": 0.3,
        "F": 0.2,
        "G High": 0.1,
        "A High": 0,
        "B High": -0.1,
        "C High": -0.2,
        "D High": -0.3,
        "E High": -0.4,
        "wild": -0.5,
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
        self.note.rect.x = self.bar.rect.x
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
