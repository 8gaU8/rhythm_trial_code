# from serial import Serial
from psychopy import core

from .dummy_serial import Serial
from .utils import fire_and_forget

connected = True
PULSE_WIDTH = 0.01


def read_thread(port: Serial):
    while connected:
        if port.in_waiting > 0:
            print("0x%X" % (port.read(1)))


@fire_and_forget
def fire(data):
    global port
    port.write(data)
    core.wait(PULSE_WIDTH)
    port.write


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
