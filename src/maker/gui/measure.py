"""Measure of Notes on a Bar Manager"""

__author__="Tyler Westland"

import pygame

from maker.gui.note_on_bar import NoteOnBar

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

    def to_wave_file(self) -> :
        notes = ""
        for row in self.rows:
            for note in row:


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
