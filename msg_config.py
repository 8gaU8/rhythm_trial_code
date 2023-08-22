from typing import List

from serial import Serial

BASE_TIMES = 3

from .message import (
    Message,
    play_none,
    play_sound_trigger_factory,
    play_trigger_factory,
)


def build_base_msgs(port: Serial) -> List[Message]:
    play_trigger_1 = play_trigger_factory(port, [1])
    play_trigger_234 = play_trigger_factory(port, [2])
    play_trigger_on_note = play_trigger_factory(port, [3])
    play_sound_trigger = play_sound_trigger_factory(play_trigger_on_note)
    msg_series = [
        Message(play_sound_trigger, time=0),
        Message(play_trigger_1, time=0),
        Message(play_sound_trigger, time=0.375),
        Message(play_trigger_234, time=0.5),
        Message(play_sound_trigger, time=0.75),
        Message(play_trigger_234, time=1.0),
        Message(play_sound_trigger, time=1.25),
        Message(play_sound_trigger, time=1.5),
        Message(play_trigger_234, time=1.5),
        Message(play_none, time=2.0),
    ]
    return msg_series


def build_trigger_msgs(port: Serial) -> List[Message]:
    play_trigger_1 = play_trigger_factory(port, [1])
    play_trigger_234 = play_trigger_factory(port, [2])
    msg_series = [
        Message(play_trigger_1, time=0),
        Message(play_trigger_234, time=0.5),
        Message(play_trigger_234, time=1.0),
        Message(play_trigger_234, time=1.5),
        Message(play_trigger_1, time=2.0),
    ]
    return msg_series


def build_probe_tone(port: Serial) -> List[Message]:
    play_trigger_on_note = play_trigger_factory(port, [3])
    play_sound_trigger = play_sound_trigger_factory(play_trigger_on_note)
    msg_series = [
        Message(play_sound_trigger, time=0.0),
    ]
    return msg_series
