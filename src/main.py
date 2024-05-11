import config
from modes.learner import ChordGameFSM
from piano_display import PianoDisplay
import pygame
import sys


class ReaderFSM:
    def __init__(self):
        device_id = 0  # Change as needed for your MIDI device
        self.midi_backend = config.MIDI_BACKEND_CLS(device_id)
        self.display = PianoDisplay()

        mode = config.START_MODE
        self.game = mode(self.display)

    def run(self):
        running = True
        while running:
            self.display.draw_staff()  # Background must be drawn first

            # Pull notes and update game
            notes = self.midi_backend.poll_input()
            self.game.step(notes)

            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()
        sys.exit()


    #-------------------------------------
    #   State Machine
    #-------------------------------------

    def state_handler(self):
        pass

if __name__ == "__main__":
    reader = ReaderFSM()
    reader.run()
