from typing import List

from serial import Serial

from .message import Message, play_none, play_sound, play_trigger_factory

SCALE = 1.0
BASE_TIME = 3


def build_base_msgs(port: Serial) -> List[Message]:
    play_trigger = play_trigger_factory(port)
    msg_series = [
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
    return msg_series


def build_trigger_msgs(port: Serial) -> List[Message]:
    play_trigger = play_trigger_factory(port)
    msg_series = [
        Message(play_trigger, time=0),
        Message(play_trigger, time=0.5),
        Message(play_trigger, time=1.0),
        Message(play_trigger, time=1.5),
        Message(play_trigger, time=2.0),
    ]
    return msg_series


def build_probe_tone(port: Serial) -> Message:
    msg = Message(play_sound, time=0.0)
    return msg
