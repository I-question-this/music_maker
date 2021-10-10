"""Measure of Notes on a Bar Manager"""

__author__="Tyler Westland"

import random
random.seed()
import pygame

from maker.gui.note_on_bar import NoteOnBar
from maker.music.tune import Tune


class Measure():
    def __init__(self, rows:int, columns:int, group:pygame.sprite.Group,
            x:int=0, y:int=0):
        if rows < 1:
            raise ValueError("There must be at least one row")
        
        if columns < 1:
            raise ValueError("There must be at least one column")

        self.rows = []
        for row_num in range(rows):
            row = []
            for col_num in range(columns):
                row.append(NoteOnBar(group))
            self.rows.append(row)

        # Move all of them to the correct placement
        self.move(x, y)

    def to_tune(self) -> Tune:
        note_codes = []
        for row in self.rows:
            for note in row:
                # Set note letter aside
                note_code = note.note.note

                # Handle wild case
                if note_code == "wild":
                    while note_code == "wild":
                        note_code = random.choice(
                                list(NoteOnBar.NOTE_POSITIONS))

                # Handle more special cases
                if note_code == "hold":
                    if len(note_codes) == 0:
                        note_codes.append("R")
                    else:
                        note_codes.append(note_codes[-1])
                elif note_code == "rest":
                    note_codes.append("R")
                else:
                    note_codes.append(note_code)

        # Create Tune object
        print(note_codes)
        return Tune(note_codes)

    def move(self, x:int, y:int):
        self.x = x
        self.y = y
        width = self.rows[0][0].bar.rect.width
        height = self.rows[0][0].bar.rect.height
        for row_num in range(len(self.rows)):
            for col_num in range(len(self.rows[row_num])):
                self.rows[row_num][col_num].move(
                        x + width * col_num,
                        y + height * 1.5 * row_num)

    def check_mouse_click(self, mousex:int, mousey:int):
        mousex, mousey = pygame.mouse.get_pos()
        mouse_rect = pygame.Rect((mousex, mousey), (0,0))
        for row in self.rows:
            for note in row:
                if note.note.rect.contains(mouse_rect):
                    note.update()
                    break
