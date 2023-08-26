import asyncio
import time

from psychopy import core
from pygame import mixer


def wait_until(target_time: float):
    sleep_time = target_time - time.time()
    if sleep_time < 0:
        return
    core.wait(sleep_time)
    return


def init_sound_player():
    # init sound player
    freq = 44100  # audio CD quality
    bitsize = -16  # unsigned 16 bit
    channels = 1  # 1 is mono, 2 is stereo
    buffer = 1024  # number of samples
    mixer.init(freq, bitsize, channels, buffer)
    mixer.music.set_volume(0.8)


def fire_and_forget(func):
    def wrapper(*args, **kwargs):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        return loop.run_in_executor(None, func, *args, *kwargs)

    return wrapper
