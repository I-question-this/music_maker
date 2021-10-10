__author__="Aaron Ruen"

def adjust_frequency(base_freq, num_twelfths, up = True):
    if up:
        new_freq = round(base_freq * ((2**(1/12))**num_twelfths), 2)
    else:
        new_freq = round(base_freq * ((2**(1/12))**(-num_twelfths)), 2)
    return new_freq

class Note():
    def __init__(self, name, octave, frequency, length, add_harm=True):
        self.name = name
        self.octave = octave
        self.frequency = frequency
        self.length = length
        self.add_harmonics = add_harm
    
    def down_octave(self):
        self.octave -= 1
        self.frequency = adjust_frequency(self.frequency, num_twelfths=12, up=False)

NOTES = {
    "A": Note(name = "A", octave = 4, frequency = 440, length = 0.25), 
    "A#": Note(name = "A#", octave = 4, frequency = adjust_frequency(440, 1), length = 0.25), 
    "B": Note(name = "B", octave = 4, frequency = adjust_frequency(440, 2), length = 0.25),
    "C": Note(name = "C", octave = 4, frequency = adjust_frequency(440, 3), length = 0.25),
    "C#": Note(name = "C#", octave = 4, frequency = adjust_frequency(440, 4), length = 0.25),
    "D": Note(name = "D", octave = 4, frequency = adjust_frequency(440, 5), length = 0.25),
    "D#": Note(name = "D#", octave = 4, frequency = adjust_frequency(440, 6), length = 0.25),
    "E": Note(name = "E", octave = 4, frequency = adjust_frequency(440, 7), length = 0.25),
    "F": Note(name = "F", octave = 4, frequency = adjust_frequency(440, 8), length = 0.25),
    "F#": Note(name = "F#", octave = 4, frequency = adjust_frequency(440, 9), length = 0.25),
    "G": Note(name = "G", octave = 4, frequency = adjust_frequency(440, 10), length = 0.25),
    "G#": Note(name = "G#", octave = 4, frequency = adjust_frequency(440, 11), length = 0.25),
}