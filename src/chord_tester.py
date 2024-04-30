import random

class ChordTester:
    def __init__(self):
        self.chords = {
            "C": {"C"},
            "Dm": {"D"},
            "Em": {"E"},
            "F": {"F"},
            "G": {"G"},
            "Am": {"A"},
            #"C": {"C", "E", "G"},
            #"Dm": {"D", "F", "A"},
            #"Em": {"E", "G", "B"},
            #"F": {"F", "A", "C"},
            #"G": {"G", "B", "D"},
            #"Am": {"A", "C", "E"},
        }
        assert len(self.chords) > 1, "Must define more than 1 chords"
        self.current_chord = None
        self.current_chord_notes = set()

    def select_random_chord(self):
        _last = self.current_chord
        while self.current_chord == _last:
            self.current_chord, chord_notes = random.choice(list(self.chords.items()))
        self.current_chord_notes = chord_notes
        return self.current_chord, self.current_chord_notes

    def compare_notes(self, played_notes):
        # Normalize played notes to note names
        notes = {(note, self.note_number_to_name(note)) for note in played_notes}

        correct = {note[0] for note in notes if note[1] in self.current_chord_notes}
        incorrect = {note[0] for note in notes if note[1] not in self.current_chord_notes}
        success = (len(correct) == len(self.current_chord_notes)) & (len(incorrect) == 0)

        return correct, incorrect, success

    @staticmethod
    def note_number_to_name(note_number):
        note_names = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        return note_names[note_number % 12]