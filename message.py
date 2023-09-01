from typing import List, Protocol

from pygame import mixer
from serial import Serial

from .dummy_serial import DummySerial
from .serial_trigger import fire


# Annotation Class for play functions
class PlayFuncType(Protocol):
    __name__: str

    def __call__(self, sound: bool) -> None:
        ...


class Message:
    time_scale: float = 1.0

    def __init__(self, play: PlayFuncType, time: float):
        self.org_time = time
        self.time = time * self.time_scale
        self._play: PlayFuncType = play

    def play(self, sound: bool) -> None:
        self._play(sound=sound)

    def __repr__(self) -> str:
        return f"Message({self._play.__name__}, time={self.time})"

    def __str__(self) -> str:
        return self.__repr__()


class PlayFactories:
    def __init__(self, soundfiles: "list[str]") -> None:
        self.sounds = []
        for file in soundfiles:
            self.sounds.append(mixer.Sound(file))

    # play functions
    def play_none(self, sound: bool) -> None:
        # return True
        ...

    def note_fctr(self, ch_id: int) -> PlayFuncType:
        def play_sound(sound: bool):
            if sound:
                mixer.Channel(ch_id).play(self.sounds[ch_id])

        return play_sound

    def trig_fctr(self, port: "Serial|DummySerial", data: List[int]) -> PlayFuncType:
        def play_trigger(sound: bool) -> None:
            fire(port, data)

        return play_trigger

    def note_trig_fctr(
        self,
        play_trigger: PlayFuncType,
        play_sound: PlayFuncType,
    ) -> PlayFuncType:
        def play_sound_trigger(sound: bool):
            play_sound(sound)
            play_trigger(sound)

        return play_sound_trigger
