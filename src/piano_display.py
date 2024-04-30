import pygame
from config import PianoConfig

class PianoDisplay:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((PianoConfig.WIDTH, PianoConfig.HEIGHT))
        self.font = pygame.font.SysFont(None, 24)
        self.note_image = PianoConfig.load_resources()
        self.key_map, self.accidentals = PianoConfig.setup_key_map()
        self.note_map = PianoConfig.setup_note_map()

        self.funcs = {}

    ### Staff and notes ###
    def draw_staff(self):
        self.screen.fill((255, 255, 255))
        
        for i in range(5):
            pygame.draw.line(self.screen, (0, 0, 0), (60, PianoConfig.OFFSET + PianoConfig.INTERVAL * i), (260, PianoConfig.OFFSET + PianoConfig.INTERVAL * i))
            pygame.draw.line(self.screen, (0, 0, 0), (60, PianoConfig.OFFSET + PianoConfig.INTERVAL * (7 + i)), (260, PianoConfig.OFFSET + PianoConfig.INTERVAL * (7 + i)))

    def draw_notes(self, correct_notes, incorrect_notes):
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
        
    ### Text displays ###
    def display_chord(self, chord_name):
        """Display the name of the chord on the top part of the screen."""
        #self.clear_screen()
        self.render_text(chord_name, (self.screen.get_width() // 2, 100))

    def display_feedback(self, feedback):
        """Display feedback message at the bottom part of the screen."""
        self.render_text(feedback, (self.screen.get_width() // 2, 500))

    def render_text(self, text, position):
        """Utility method to render text at a given position."""
        text_surface = self.font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=position)
        self.screen.blit(text_surface, text_rect)