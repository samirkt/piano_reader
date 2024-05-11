import midi_backend
from modes import learner, practice

MIDI_BACKEND_CLS = midi_backend.TestMidiBackend
START_MODE = learner.ChordGameFSM #practice.ChordViz