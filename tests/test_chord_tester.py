import unittest
from src import chord_tester

class TestChordTester(unittest.TestCase):
    def test_compare_notes(self):
        self.chord_tester = chord_tester.ChordTester()
        self.chord_tester.chords = {"C": {"C", "E", "G"}}
        notes = [0,12]
        correct, incorrect, success = self.chord_tester.compare_notes(notes)
        breakpoint()

if __name__ == "__main__":
    unittest.main()