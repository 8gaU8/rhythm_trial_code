from typing import List

from serial import Serial

BASE_TIMES = 3

from .dummy_serial import DummySerial
from .message import Message, PlayFactories


def build_base_msgs(
    port: "Serial|DummySerial", pf: PlayFactories, base_time: float
) -> List[Message]:
    pt1 = pf.trig_fctr(port, [1])
    pt234 = pf.trig_fctr(port, [2])

    play_trig_on_note = pf.trig_fctr(port, [3])
    note_h = pf.note_fctr(0)
    note = pf.note_fctr(1)

    pnth = pf.note_trig_fctr(note_h, play_trig_on_note)
    pnt = pf.note_trig_fctr(note, play_trig_on_note)

    t = lambda time: (time + base_time)

    msg_series = [
        Message(pnth, t(0)),
        Message(pt1, t(0)),
        Message(pnt, t(0.375)),
        Message(pt234, t(0.5)),
        Message(pnt, t(0.75)),
        Message(pt234, t(1.0)),
        Message(pnt, t(1.25)),
        Message(pnt, t(1.5)),
        Message(pt234, t(1.5)),
        Message(pf.play_none, t(2.0)),
    ]
    return msg_series


def build_trigger_msgs(
    port: "Serial|DummySerial", pf: PlayFactories, base_time: float, delay: float
) -> List[Message]:
    pt1 = pf.trig_fctr(port, [1])
    pt234 = pf.trig_fctr(port, [2])
    play_trig_on_note = pf.trig_fctr(port, [3])
    pn = pf.note_fctr(0)
    pnt = pf.note_trig_fctr(pn, play_trig_on_note)

    t = lambda time: (time + base_time)

    msg_series = [
        Message(pnt, t(0)),
        Message(pt1, t(0)),
        Message(pt234, t(0.5)),
        Message(pt234, t(1.0)),
        Message(pt234, t(1.5)),
        Message(pt1, t(2.0)),
        Message(pnt, t(2.0) + delay),
    ]
    return msg_series
