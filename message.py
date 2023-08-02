from copy import deepcopy
from typing import List, Protocol

from pygame import mixer
from serial import Serial

from .serial_trigger import fire


# Annotation Class for play functions
class PlayFuncType(Protocol):
    __name__: str

    def __call__(self, sound: bool) -> None:
        ...


class Message:
    time_scale: float = 1.0

    def __init__(self, play: PlayFuncType, time: float):
        self.time = time * self.time_scale
        self._play: PlayFuncType = play

    def play(self, sound: bool) -> None:
        self._play(sound=sound)

    def __repr__(self) -> str:
        return f"Message({self._play.__name__}, time={self.time})"

    def __str__(self) -> str:
        return self.__repr__()


# play functions
def play_sound(sound: bool) -> None:
    if sound:
        mixer.music.play()


def play_none(sound: bool) -> None:
    # return True
    ...


def play_trigger_factory(port: Serial) -> PlayFuncType:
    def play_trigger(sound: bool) -> None:
        fire(port, [2])

    return play_trigger


def get_stim_series(
    base_msgs: List[Message],
    base_times: int,
    trigger_msgs: List[Message],
    probe_delay: float,
    probe_tone: Message,
) -> List[Message]:
    # [base] [base] ... [base] [trigger] [delay time] [probe tone]
    stim_series: List[Message] = []

    stim_series.extend(base_msgs)

    # repeat base msgs for base_times
    last_time = base_msgs[-1].time
    for count in range(1, base_times):
        tmp_base_msgs = deepcopy(base_msgs)
        for msg in tmp_base_msgs:
            msg.time += count * last_time
        stim_series.extend(tmp_base_msgs)

    # append trigger msgs
    last_time = stim_series[-1].time
    tmp_triger_msgs = deepcopy(trigger_msgs)
    for msg in tmp_triger_msgs:
        msg.time += last_time
    stim_series.extend(tmp_triger_msgs)

    # add Probe Tone to stim series
    tmp_probe_tone = deepcopy(probe_tone)
    tmp_probe_tone.time += tmp_triger_msgs[-1].time + probe_delay
    stim_series.append(tmp_probe_tone)

    # sort by time
    stim_series = sorted(stim_series, key=lambda msg: msg.time)

    return stim_series
