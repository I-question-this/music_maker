#!/usr/bin/env python3
"""Tunable Tune of Notes"""

__author__="Aaron Ruen, Tyler Westland"
import re
from synthesizer import Synthesizer, Waveform, Writer
import numpy as np
from maker.music.note import Note, NOTES, adjust_frequency
import copy
import json

EASTEREGGS = {
    "Dies Irae": ['G', 'F', 'G', 'E Low'],
    "Parry Hotter": ['B Low', 'E Low', 'G', 'F', 'E Low', 'E Low', 'B', 'A', 'A', 'A', 'F'],
    "Bokemon": ['A', 'A', 'A', 'A', 'A', 'G', 'E Low', 'C Low'],
    "Boruto": ['A Low', 'E Low', 'D Low', 'G', 'G', 'D Low', 'D Low', 'E Low', 'E Low'],
    "Boring": ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R']
    }

# Keys go A, B, C, D, E, F, G
KEYS = {
    "C": {},
    "G": {"F": "F#"},
    "D": {"C": "C#", "F": "F#"},
    "A": {"C": "C#", "F": "F#", "G":"G#"},
    "E": {"C": "C#", "D":"D#", "F": "F#", "G":"G#"},
    "B": {"A": "A#", "C": "C#", "D":"D#", "F": "F#", "G":"G#"},
    "F#": {"A": "A#", "C": "C#", "D":"D#", "E":"F", "F": "F#", "G":"G#"}, 
    "C#": {"A": "A#", "B":"C", "C": "C#", "D":"D#", "E":"F", "F": "F#", "G":"G#"},
    "F": {"B":"A#"},
    "Bb": {"B":"A#", "E":"D#"},
    "Eb": {"A":"G#", "B":"A#", "E":"D#"},
    "Ab": {"A":"G#", "B":"A#", "D":"C#", "E":"D#"},
    "Db": {"A":"G#", "B":"A#", "D":"C#", "E":"D#", "G":"F#"},
    "Gb": {"A":"G#", "B":"A#", "C":"B", "D":"C#", "E":"D#", "G":"F#"},
    "Cb": {"A":"G#", "B":"A#", "C":"B", "D":"C#", "E":"D#", "F":"E", "G":"F#"},
}

def is_egg_in_tune(egg:list, song:list):
    # .: wild card
    # *: 0 or more
    # .*: O or more of anything
    egg_re = re.compile(".*"+ "".join(egg) + ".*")
    return egg_re.match("".join(song)) is not None


class Tune():
    def __init__(self, letter_representation, tempo=250, base_volume=1, key_signature = "C#"):
        self.letter_representation = letter_representation
        self.mood = None
        self.notes = []
        self.tempo = tempo # default tempo = 100 because science
        self.base_volume = base_volume # Default 1 (amplitude for square waves)
        self.easter_eggs = self.check_easter_eggs()
        self.key_signature = key_signature
        # Run function during init
        self.letter_to_notes()
        self.adjust_note_length()

    def to_dict(self) -> dict:
        return {
            "letter_representation": self.letter_representation,
            "tempo": self.tempo,
            "base_volume": self.base_volume,
            "key_signature": self.key_signature
            }

    @classmethod
    def from_dict(cls, d:dict) -> "Tune":
        return cls(
                letter_representation=d["letter_representation"],
                tempo=d["tempo"],
                base_volume=d["base_volume"],
                key_signature=d["key_signature"]
                )

    # Changes the letter representation from pygame to note objects
    def letter_to_notes(self):
        for note in self.letter_representation:
            self.notes.append(copy.copy(NOTES[note]))
        self.key_signature_adjustment()
        """
        for note in self.letter_representation:          
            self.notes.append(copy.copy(NOTES[note]))
            if self.notes[-1].name == "G#" and (self.key_signature in ["F", "Bb", "Eb", "Ab", "Db", "Gb", "Cb"]) and note== "G Low":
                self.notes[-1].down_octave()
        """
        return

    # Adjusts notes based on the key signature
    def key_signature_adjustment(self):
        for i in range(len(self.notes)):
            for key in KEYS[self.key_signature]:
                if self.notes[i].name == key:
                    if self.notes[i].octave == 3:
                        self.notes[i].frequency = adjust_frequency(NOTES[key].frequency, 12, up=False)
                    if self.notes[i].octave == 4:
                        self.notes[i].frequency = NOTES[key].frequency
                    self.notes[i].name = KEYS[self.key_signature][key]
                    break
        return

    # Adjusts default note length to the length specified by the tempo
    def adjust_note_length(self):
        for note in self.notes:
            note.length = 60/self.tempo
        return

    # Checks for easter eggs :)
    def check_easter_eggs(self) -> list:
        egglist = []
        for key in EASTEREGGS:
            if(is_egg_in_tune(EASTEREGGS[key],  self.letter_representation)):
                egglist.append(key)
        return egglist

    # Creates waveform and saves it to file
    def save_to_file(self, filename="test.wav"):
        synthesizer = Synthesizer(osc1_waveform=Waveform.square, osc1_volume=self.base_volume, use_osc2=False)
        wave = synthesizer.generate_chord([1], 0.01)

        for note in self.notes:
            temp_chord = [note.frequency]
            if note.add_harmonics == True:
                temp_chord.append(note.frequency*(1/2))
                temp_chord.append(note.frequency*2)
                temp_chord.append(note.frequency*3)
            temp_wave = synthesizer.generate_chord(temp_chord, note.length)
            wave = np.append(wave, temp_wave)

        writer = Writer()
        writer.write_wave(filename, wave)
        return

# Execute only if this file is being run as the entry file.
if __name__ == "__main__":
    letter_representation = ['A','A', 'C', 'B', 'B', 'A', 'A', 'A', 'E', 'E', 'D', 'D', 'D', 'D', 'B', 'B'] # Note names from Pygame game
    test_rage = Tune(letter_representation, key_signature="B")
    with open("test_rage.json", "w") as fout:
        json.dump(test_rage.to_dict(), fout, indent=2)

    test_happy = Tune(letter_representation, key_signature="C")
    with open("test_happy.json", "w") as fout:
        json.dump(test_happy.to_dict(), fout, indent=2)

    test_sad = Tune(letter_representation, key_signature="Db")
    with open("test_sad.json", "w") as fout:
        json.dump(test_sad.to_dict(), fout, indent=2)
