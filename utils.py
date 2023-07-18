import time

from psychopy import core
from pygame import mixer


def wait_until(target_time: float):
    sleep_time = target_time - time.time()
    if sleep_time < 0:
        return
    core.wait(sleep_time)
    return


def init_sound_player(stim_sound_file):
    # init sound player
    freq = 44100  # audio CD quality
    bitsize = -16  # unsigned 16 bit
    channels = 1  # 1 is mono, 2 is stereo
    buffer = 1024  # number of samples
    mixer.init(freq, bitsize, channels, buffer)
    mixer.music.set_volume(0.8)
    mixer.music.load(stim_sound_file)
