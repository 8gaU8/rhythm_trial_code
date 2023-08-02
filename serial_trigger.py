import time
from typing import List

from serial import Serial

from .utils import fire_and_forget

connected = True
PULSE_WIDTH = 0.05


def read_thread(port: Serial):
    while connected:
        if port.in_waiting > 0:
            print(port.read(1))


def fire(port: Serial, data: List[int]):
    print(time.time())
    port.write(data)
    sleep_and_reset(port)


@fire_and_forget
def sleep_and_reset(port: Serial):
    time.sleep(PULSE_WIDTH)
    port.write([0])
