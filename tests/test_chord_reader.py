import unittest
from src import chord_reader

class TestChordReader(unittest.TestCase):
    def test_compare_notes(self):
        self.chord_reader = chord_reader.ChordReader()
        self.chord_reader.chords = {"C": {"C", "E", "G"}}
        self.chord_reader.select_random_chord()

        notes = [0,12,4,7]
        correct, incorrect, success = self.chord_reader.compare_notes(notes)
        self.assertTrue(success)

if __name__ == "__main__":
    unittest.main()