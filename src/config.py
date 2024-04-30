import pygame

class PianoConfig:
    WIDTH = 500
    HEIGHT = 640
    INTERVAL = 20
    OFFSET = 220
    TOP = INTERVAL * 2
    MIDDLE_C = 540

    @staticmethod
    def load_resources():
        note_im_raw = pygame.image.load('whole-note.png')
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
        return {0: 'C', 1: 'C#', 2: 'D', 3: 'D#', 4: 'E', 5: 'F', 
                6: 'F#', 7: 'G', 8: 'G#', 9: 'A', 10: 'A#', 11: 'B'}
