import logging
import time

import numpy as np
from serial import Serial

from .dummy_serial import DummySerial
from .message import Message, PlayFactories
from .msg_config import BASE_TIMES, build_base_msgs, build_trigger_msgs
from .utils import init_sound_player, wait_until


def build_stim(
    port: "Serial | DummySerial",
    delay: float,
    scale: float,
    soundfiles: "list[str]",
) -> "list[Message]":
    # change all time_scale via class var
    Message.time_scale = scale
    init_sound_player()
    pf = PlayFactories(soundfiles)

    # build base msgs
    stim_series = []
    last_time = build_base_msgs(port, pf, 0)[-1].org_time
    base_time = 0
    for i in range(BASE_TIMES):
        base_time = i * last_time
        print(base_time)
        base_series = build_base_msgs(port, pf, base_time)
        stim_series.extend(base_series)

    # build trigger msgs
    trigger_msgs = build_trigger_msgs(port, pf, (base_time + last_time), delay)
    stim_series.extend(trigger_msgs)
    last_time = stim_series[-1].org_time

    # sort by time
    stim_series = sorted(stim_series, key=lambda msg: msg.time)
    return stim_series


def play_stim(stim_series: "list[Message]", sound: bool = True) -> "(float,float)":
    # play the sound stim series
    error_list = []

    start_time = time.time()
    for msg in stim_series:
        wait_until(start_time + msg.time)
        msg.play(sound=sound)
        logging.info(msg)
        error_list.append((time.time() - start_time) - msg.time)
        print(time.time() - start_time)

    # calc error
    # mean and std var of error
    diff_array = np.array(error_list)
    mean = diff_array.mean()
    std = diff_array.std()

    print(f"error is {mean} ± {std} sec")
    return start_time, stim_series[-1].time


# build stim series and run
def run_stim(
    port: "Serial | DummySerial",
    delay: float,
    scale: float,
    soundfiles: "list[str]",
    sound: bool = True,
):
    # change all time_scale via class var
    Message.time_scale = scale
    init_sound_player()
    pf = PlayFactories(soundfiles)

    # build base msgs
    stim_series = []
    last_time = build_base_msgs(port, pf, 0)[-1].org_time
    base_time = 0
    for i in range(BASE_TIMES):
        base_time = i * last_time
        print(base_time)
        base_series = build_base_msgs(port, pf, base_time)
        stim_series.extend(base_series)

    # build trigger msgs
    trigger_msgs = build_trigger_msgs(port, pf, (base_time + last_time), delay)
    stim_series.extend(trigger_msgs)
    last_time = stim_series[-1].org_time

    # sort by time
    stim_series = sorted(stim_series, key=lambda msg: msg.time)

    print(stim_series)

    # play the sound stim series
    error_list = []

    start_time = time.time()
    for msg in stim_series:
        wait_until(start_time + msg.time)
        msg.play(sound=sound)
        logging.info(msg)
        error_list.append((time.time() - start_time) - msg.time)
        print(time.time() - start_time)

    # calc error
    # mean and std var of error
    diff_array = np.array(error_list)
    mean = diff_array.mean()
    std = diff_array.std()

    print(f"error is {mean} ± {std} sec")
    return start_time, stim_series[-1].time
