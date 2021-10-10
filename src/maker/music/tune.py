__author__="Aaron Ruen"
import re
from synthesizer import Synthesizer, Waveform, Writer
import numpy as np
from note import Note, NOTES

EASTEREGGS = {
    "Dies Irae": ['G', 'E', 'G', 'F']
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
    def __init__(self, tempo=150, base_volume=1, key_signature = "C#"):    
        self.mood = None
        self.letter_representation = ['A','A', 'C', 'B', 'B', 'A', 'A', 'A', 'E', 'E', 'D', 'D', 'D', 'D', 'B', 'B'] # Note names from Pygame game
        self.notes = []
        self.tempo = tempo # default tempo = 100 because science
        self.base_volume = base_volume # Default 1 (amplitude for square waves)
        self.easter_eggs = self.check_easter_eggs()
        self.key_signature = key_signature
        # Run function during init
        self.letter_to_notes()
        self.adjust_note_length()

    # Changes the letter representation from pygame to note objects
    def letter_to_notes(self):
        self.key_signature_adjustment()
        for note in self.letter_representation:          
            self.notes.append(NOTES[note])
        return

    # Adjusts default note length to the length specified by the tempo
    def adjust_note_length(self):
        for note in self.notes:
            note.length = 60/self.tempo
        return

    # Checks for easter eggs :)
    def check_easter_eggs(self):
        egglist = []
        for key in EASTEREGGS:
            if(is_egg_in_tune(EASTEREGGS[key],  self.letter_representation)):
                egglist.append(key)
        return egglist

    # Changes Duty Cycle
    def adjust_duty_cycle(self, new_duty_cycle):
        for note in self.notes:
            note.duty_cycle = new_duty_cycle * 100
        return

    def key_signature_adjustment(self):
        for i in range(len(self.letter_representation)):
            for key in KEYS[self.key_signature]:
                if self.letter_representation[i] == key:
                    self.letter_representation[i] = KEYS[self.key_signature][key]
                    break
        return

    # Creates waveform and saves it to file
    def save_to_file(self, filename="test2.wav"):
        synthesizer = Synthesizer(osc1_waveform=Waveform.square, osc1_volume=1, use_osc2=False)
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
        print(f"Filename {filename} written")
        return

test = Tune()
test.save_to_file()