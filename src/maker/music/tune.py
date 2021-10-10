__author__="Aaron Ruen"
import re
import chippy
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

    def additive_synthesis(self, wave1, wave2):
        test1 = np.array(bytearray(wave1))
        test2 = np.array(bytearray(wave2))
        test3 = np.empty(shape=test1.shape)
        for i in range(len(test1)):
            test3[i] = (test1[i] + test2[i])
            # print(test3[i])
            #print(test3[i])
        wave1 = bytes(test3)
        print(wave1[89])
        return wave1

    # Creates waveform and saves it to file
    def save_to_file(self, filename="test.wav"):
        synth = chippy.Synthesizer(framerate = 44100)
        waveform = synth.pulse_pcm(length=0.001, frequency=10, duty_cycle=0)
        waveform2 = synth.pulse_pcm(length=0.001, frequency=10, duty_cycle=0)
        waveform3 = synth.pulse_pcm(length=0.001, frequency=10, duty_cycle=0)
        for note in self.notes:
            temp_wave = synth.pulse_pcm(length=note.length, frequency=note.frequency, duty_cycle=note.duty_cycle)
            if note.add_harmonics == True:
                temp_wave_harm = synth.pulse_pcm(length=note.length, frequency=note.frequency*2, duty_cycle=note.duty_cycle)
                temp_wave2 = self.additive_synthesis(temp_wave, temp_wave_harm)
            if note.add_duty == True:
                temp_wave_duty = synth.pulse_pcm(length=note.length, frequency=note.frequency, duty_cycle=note.duty_cycle/2)
                temp_wave3 = self.additive_synthesis(temp_wave, temp_wave_duty)
            waveform += temp_wave
            waveform2 += temp_wave2
            waveform3 += temp_wave3
        synth.save_wave(waveform, filename)
        synth.save_wave(waveform2, "test2.wav")
        synth.save_wave(waveform3, "test3.wav")
        return

test = Tune()
test.save_to_file()