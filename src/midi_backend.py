import pygame.midi
import time

class MidiBackend:
    def __init__(self, midi_input_id=0):
        pygame.midi.init()
        self.midi_input = pygame.midi.Input(midi_input_id)
        self.notes = set()

    def poll_input(self):
        if self.midi_input.poll():
            event = self.midi_input.read(1)[0]
            [status, note_number, velocity, _] = event[0]
            if status == 144:
                if velocity != 0:
                    self.notes.add(note_number)
                else:
                    self.notes.remove(note_number)
        return self.notes

class TestMidiBackend:
    def __init__(self, midi_input_id=0):
        self.notes = set()

    def poll_input(self):
        base = int(time.time() // 4 % 4) + 40
        return [base, base + 4, base + 7]