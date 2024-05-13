import time

from chord_reader import ChordReader


class GameState:
    INIT = 0
    RUN = 1

class ChordViz:
    CHORD_VALID_DELAY = 0.5  # Delay after a correct chord before resetting

    def __init__(self, display):
        self.display = display
        self.chord_reader = ChordReader()
        self.state = GameState.INIT
        self.current_chord_name = ""

    def step(self, notes):
        self.current_chord_name = self.chord_reader.get_chord(notes)

        self.update_display(self.current_chord_name, notes)
        self.state_handler()

    def update_display(self, chord_name, notes):
        self.display.display_chord(chord_name)
        self.display.draw_notes(notes)

    #-------------------------------------
    #   State Machine
    #-------------------------------------

    def state_handler(self):
            if self.state == GameState.INIT:
                self.state = GameState.RUN
            elif self.state == GameState.RUN:
                pass