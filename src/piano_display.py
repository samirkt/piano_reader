import os
import pygame
import src


class PianoConfig:
    WIDTH = 500
    HEIGHT = 640
    INTERVAL = 20
    OFFSET = 220
    TOP = INTERVAL * 2
    MIDDLE_C = 540

    @staticmethod
    def load_resources():
        # Get path to note image based on src directory location
        note_path = os.path.join(os.path.dirname(src.__file__), 'whole-note.png')
        note_im_raw = pygame.image.load(note_path)
        w, h = note_im_raw.get_rect().size
        return pygame.transform.scale(note_im_raw, ((w * 20) // h, 20))

    @staticmethod
    def setup_key_map():
        acc_inds = {1, 3, 6, 8, 10}
        key_map = {}
        accidentals = set()
        loc = PianoConfig.TOP + (PianoConfig.INTERVAL * 27)
        for i in range(21, 110):
            if i == 62:
                loc -= PianoConfig.INTERVAL
            if i % 12 not in acc_inds:
                loc -= PianoConfig.INTERVAL * 0.5
            else:
                accidentals.add(i)
            key_map[i] = loc
        return key_map, accidentals

    @staticmethod
    def setup_note_map():
        return {0: 'C', 1: 'C#/Db', 2: 'D', 3: 'D#/Eb', 4: 'E', 5: 'F', 
                6: 'F#/Gb', 7: 'G', 8: 'G#/Ab', 9: 'A', 10: 'A#/Bb', 11: 'B'}

class PianoDisplay:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((PianoConfig.WIDTH, PianoConfig.HEIGHT))
        self.font = pygame.font.SysFont(None, 24)
        self.note_image = PianoConfig.load_resources()
        self.key_map, self.accidentals = PianoConfig.setup_key_map()
        self.note_map = PianoConfig.setup_note_map()

        self.funcs = {}

    #-------------------------------------
    #   Notation displays
    #-------------------------------------

    def draw_staff(self):
        self.screen.fill((255, 255, 255))
        
        for i in range(5):
            pygame.draw.line(self.screen, (0, 0, 0), (60, PianoConfig.OFFSET + PianoConfig.INTERVAL * i), (260, PianoConfig.OFFSET + PianoConfig.INTERVAL * i))
            pygame.draw.line(self.screen, (0, 0, 0), (60, PianoConfig.OFFSET + PianoConfig.INTERVAL * (7 + i)), (260, PianoConfig.OFFSET + PianoConfig.INTERVAL * (7 + i)))

    def draw_notes(self, notes):
        _notes = {(note, (0, 255, 0)) for note in notes}

        for note_tup in _notes:
            note, color = note_tup
            note_pos = self.key_map[note] - (PianoConfig.INTERVAL * 0.5)
            txt = self.font.render(self.note_map[note % 12], True, color)
            self.screen.blit(txt, (20, note_pos - 15))
            self.screen.blit(self.note_image, (100, note_pos))
            if note == 60:
                pygame.draw.line(self.screen, (0, 0, 0), (100, PianoConfig.MIDDLE_C), (100 + self.note_image.get_width(), PianoConfig.MIDDLE_C))
        
    def draw_note_accuracy(self, correct_notes, incorrect_notes):
        _correct = {(note, (0, 255, 0)) for note in correct_notes}
        _incorrect = {(note, (255, 0, 0)) for note in incorrect_notes}
        notes = _correct | _incorrect

        for note_tup in notes:
            note, color = note_tup
            note_pos = self.key_map[note] - (PianoConfig.INTERVAL * 0.5)
            txt = self.font.render(self.note_map[note % 12], True, color)
            self.screen.blit(txt, (20, note_pos - 15))
            self.screen.blit(self.note_image, (100, note_pos))
            if note == 60:
                pygame.draw.line(self.screen, (0, 0, 0), (100, PianoConfig.MIDDLE_C), (100 + self.note_image.get_width(), PianoConfig.MIDDLE_C))
        
    #-------------------------------------
    #   Text displays
    #-------------------------------------

    def display_chord(self, chord_name):
        """Display the name of the chord on the top part of the screen."""
        self.render_text(chord_name, (self.screen.get_width() // 2, 100))

    def display_feedback(self, feedback):
        """Display feedback message at the bottom part of the screen."""
        self.render_text(feedback, (self.screen.get_width() // 2, 500))

    def render_text(self, text, position):
        """Utility method to render text at a given position."""
        text_surface = self.font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=position)
        self.screen.blit(text_surface, text_rect)