import logging
import time

import numpy as np

from .message import Message, get_stim_series
from .msg_config import BASE_TIMES, build_base_msgs, build_probe_tone, build_trigger_msgs
from .utils import init_sound_player, wait_until


def run_stim(
    port, delay: float, scale: float, stim_sound_file: str, sound: bool = True
):
    Message.time_scale = scale
    init_sound_player(stim_sound_file=stim_sound_file)

    stim_series = get_stim_series(
        base_msgs=build_base_msgs(port),
        base_times=BASE_TIMES,
        trigger_msgs=build_trigger_msgs(port),
        probe_tone=build_probe_tone(port),
        probe_delay=delay,
    )
    print(stim_series)

    error_list = []

    start_time = time.time()
    for msg in stim_series:
        wait_until(start_time + msg.time)
        msg.play(sound=sound)
        logging.info(msg)
        error_list.append((time.time() - start_time) - msg.time)

    diff_array = np.array(error_list)
    mean = diff_array.mean()
    std = diff_array.std()

    print(f"error is {mean} ± {std} sec")
    return start_time, stim_series[-1].time
