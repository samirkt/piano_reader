import random
from enum import Enum

NOTE_NAMES = [
    ["C"],
    ["C#","C#/Db"],
    ["D"],
    ["Eb", "D#/Eb"],
    ["E"],
    ["F"],
    ["F#", "F#/Gb"],
    ["G"],
    ["Ab", "G#/Ab"],
    ["A"],
    ["Bb", "A#/Bb"],
    ["B"],
]

class ChordForms(Enum):
    major = ["", [0,4,7]]
    minor = ["m", [0,3,7]]
    major7 = ["maj7", [0,4,7,11]]
    minor7 = ["m7", [0,3,7,10]]
    dom7 = ["7", [0,4,7,10]]
    maj6 = ["6", [0,4,7,9]]


class ChordReader:
    def __init__(self):
        self.chord_map = {}
        self.note_map = {}

        self.generate_maps()
        print(self.chord_map)
        assert len(self.chord_map) > 1, "Must define more than 1 chords"
        self.current_chord = None
        self.current_chord_notes = set()

    def select_random_chord(self):
        _last = self.current_chord
        while self.current_chord == _last:
            self.current_chord, chord_notes = random.choice(list(self.chord_map.items()))
        self.current_chord_notes = chord_notes
        return self.current_chord, self.current_chord_notes

    def compare_notes(self, played_notes):
        # Normalize played notes to note names
        notes = {(note, self.note_number_to_name(note)) for note in played_notes}

        chk = self.current_chord_notes.copy()
        correct, incorrect = set(), set()
        for note in notes:
            if note[1] in self.current_chord_notes:
                correct.add(note[0])
                chk.discard(note[1])
            else:
                incorrect.add(note[0])

        success = (len(chk) == 0) & (len(incorrect) == 0)

        return correct, incorrect, success
    
    def _get_note_tuple(self, notes):
        return tuple(sorted(notes))

    def generate_maps(self):
        for i, note in enumerate(NOTE_NAMES):
            for chord_form in ChordForms:
                _chord_form = chord_form.value
                chord_name = note[0] + _chord_form[0]
                notes = {self.note_number_to_name(i+x) for x in _chord_form[1]} # offset notes by root of chord

                self.chord_map[chord_name] = notes
                self.note_map[self._get_note_tuple(notes)] = chord_name
    
    def get_chord(self, notes):
        notes = {self.note_number_to_name(note) for note in notes}
        return self.note_map.get(self._get_note_tuple(notes), "")

    @staticmethod
    def note_number_to_name(note_number):
        return NOTE_NAMES[note_number % 12][-1]
    