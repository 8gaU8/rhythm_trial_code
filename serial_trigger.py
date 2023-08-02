from typing import List
import time

from psychopy import core
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
    core.wait(PULSE_WIDTH)
    port.write([0])


# # Open the Windows device manager, search for the "TriggerBox VirtualSerial Port (COM6)"
# # in "Ports /COM & LPT)" and enter the COM port number in the constructor.
# port = Serial("COM6")
# # Start the read thread
# thread = threading.Thread(target=read_thread, args=(port,))
# thread.start()
# # Set the port to an initial state
# port.write([0x00])
# time.sleep(PULSE_WIDTH)
# # Set Bit 0, Pin 2 of the Output(to Amp) connector
# port.write([0x01])
# time.sleep(PULSE_WIDTH)
# # Reset Bit 0, Pin 2 of the Output(to Amp) connector
# port.write([0x00])
# time.sleep(PULSE_WIDTH)
# # Reset the port to its default state
# port.write([0xFF])
# time.sleep(PULSE_WIDTH)
# # Terminate the read thread
# connected = False
# thread.join(1.0)
# # Close the serial port
# port.close()
