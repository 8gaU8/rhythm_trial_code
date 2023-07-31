from .message import Message, play_none, play_sound, play_trigger

SCALE = 1.0
BASE_TIME = 3


BASE_MSGS = [
    Message(play_sound, time=0),
    Message(play_trigger, time=0),
    Message(play_sound, time=0.375),
    Message(play_trigger, time=0.5),
    Message(play_sound, time=0.75),
    Message(play_trigger, time=1.0),
    Message(play_sound, time=1.25),
    Message(play_sound, time=1.5),
    Message(play_trigger, time=1.5),
    Message(play_none, time=2.0),
]


TIGGER_MSGS = [
    Message(play_trigger, time=0),
    Message(play_trigger, time=0.5),
    Message(play_trigger, time=1.0),
    Message(play_trigger, time=1.5),
    Message(play_trigger, time=2.0),
]

PROBE_TONE = Message(play_sound, time=0.0)
