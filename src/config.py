import midi_backend
from modes import learner, practice

MIDI_BACKEND_CLS = midi_backend.TestMidiBackend
#MIDI_BACKEND_CLS = midi_backend.MidiBackend
START_MODE = learner.ChordGameFSM
#START_MODE = practice.ChordViz