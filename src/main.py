import pygame
import sys
import time

from chord_tester import ChordTester
from midi_backend import MidiBackend
from piano_display import PianoDisplay

class GameState:
    INIT = 0
    WAITING = 1
    VALIDATING = 2
    UPDATING = 3

class ChordGameFSM:
    CHORD_VALID_DELAY = 0.5  # Delay after a correct chord before resetting

    def __init__(self, device_id):
        self.midi_backend = MidiBackend(device_id)
        self.display = PianoDisplay()
        self.chord_tester = ChordTester()
        self.state = GameState.INIT
        self.start_time = 0
        self.current_chord_name = ""

    def run(self):
        running = True
        while running:
            notes = self.midi_backend.poll_input()
            correct, incorrect, success = self.chord_tester.compare_notes(notes)

            self.update_display(self.current_chord_name, correct, incorrect)
            self.state_handler(success, notes)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()
        sys.exit()

    def update_display(self, chord_name, correct_notes, incorrect_notes):
        self.display.draw_staff()  # Background must be drawn first
        self.display.display_chord(chord_name)
        self.display.draw_notes(correct_notes, incorrect_notes)
        self.display_state_feedback(correct_notes, incorrect_notes)

    def display_state_feedback(self, correct_notes, incorrect_notes):
        if self.state == GameState.WAITING and (correct_notes or incorrect_notes):
            self.display.display_feedback("Try again!")
        elif self.state == GameState.UPDATING:
            self.display.display_feedback("Correct!")
    
    def state_handler(self, success, notes):
            if self.state == GameState.INIT:
                self.current_chord_name, _ = self.chord_tester.select_random_chord()
                self.state = GameState.WAITING
            elif self.state == GameState.WAITING:
                if success:
                    self.start_time = time.time()
                    self.state = GameState.VALIDATING
            elif self.state == GameState.VALIDATING:
                if not success:
                    self.state = GameState.WAITING
                if time.time() - self.start_time > ChordGameFSM.CHORD_VALID_DELAY:
                    self.state = GameState.UPDATING
            elif self.state == GameState.UPDATING:
                if not notes:
                    self.current_chord_name, _ = self.chord_tester.select_random_chord()
                    self.state = GameState.WAITING

def main():
    device_id = 0  # Change as needed for your MIDI device
    game = ChordGameFSM(device_id)
    game.run()

if __name__ == "__main__":
    main()
