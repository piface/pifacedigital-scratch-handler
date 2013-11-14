#!/usr/bin/env python3
from array import array
from time import sleep
import threading
import socket
import sys
import struct


__version__ = "2.0.3"


if "-e" in sys.argv:
    import pifacedigital_emulator as pfio
    sys.argv.remove("-e")
else:
    import pifacedigitalio as pfio


PORT = 42001
DEFAULT_HOST = '127.0.0.1'
BUFFER_SIZE = 175
SOCKET_TIMEOUT = 1

SCRATCH_SENSOR_NAME_INPUT = (
    'piface-input1',
    'piface-input2',
    'piface-input3',
    'piface-input4',
    'piface-input5',
    'piface-input6',
    'piface-input7',
    'piface-input8')

SCRATCH_SENSOR_NAME_OUTPUT = (
    'piface-output1',
    'piface-output2',
    'piface-output3',
    'piface-output4',
    'piface-output5',
    'piface-output6',
    'piface-output7',
    'piface-output8')


class ScratchListener(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.last_zero_bit_mask = 0
        self.last_one_bit_mask = 0
        self.pifacedigital = pfio.PiFaceDigital()

    def stop(self):
        self.alive = False

    def run(self):
        self.alive = True
        while self.alive:
            try:
                global scratch_socket
                data = scratch_socket.recv(BUFFER_SIZE).decode('utf-8')
                data = data[4:]  # get rid of the length info

            except socket.timeout:  # if we timeout, re-loop
                continue
            except:  # exit on any other errrors
                break

            data = data.split(" ")

            if data[0] == 'sensor-update':
                data = data[1:]
                print('received sensor-update:', data)
                self.sensor_update(data)

            elif data[0] == 'broadcast':
                data = data[1:]
                print('received broadcast:', data)

            else:
                print('received something:', data)

    def sensor_update(self, data):
        index_is_data = False  # ignore the loop contents if not sensor
        zero_bit_mask = 0  # bit mask showing where zeros should be written
        one_bit_mask = 0  # bit mask showing where ones should be written
        we_should_update_piface = False

        # go through all of the sensors that have been updated
        for i in range(len(data)):
            if index_is_data:
                index_is_data = False
                continue

            sensor_name = data[i].strip('"')

            # if this sensor is a piface output then reflect
            # that update on the board
            if sensor_name in SCRATCH_SENSOR_NAME_OUTPUT:
                we_should_update_piface = True
                pin_index = SCRATCH_SENSOR_NAME_OUTPUT.index(sensor_name)
                sensor_value = int(data[i + 1])
                index_is_data = True

                # could this be made more efficient by sending a single write
                if sensor_value == 0:
                    zero_bit_mask ^= (1 << pin_index)
                else:
                    one_bit_mask ^= (1 << pin_index)

        if we_should_update_piface:
            old_pin_bitp = self.pifacedigital.output_port.value
            new_pin_bitp = old_pin_bitp & ~zero_bit_mask  # set the zeros
            new_pin_bitp |= one_bit_mask  # set the ones

            # write the new bit pattern
            if new_pin_bitp != old_pin_bitp:
                self.pifacedigital.output_port.value = new_pin_bitp


def input_handler(event):
    """Callback function for when inputs are changed."""
    broadcast_pin_update(event.pin_num, event.direction ^ 1)


def broadcast_pin_update(pin_index, value):
    sensor_name = SCRATCH_SENSOR_NAME_INPUT[pin_index]
    bcast_str = 'sensor-update "%s" %d' % (sensor_name, value)
    print('sending:', bcast_str)
    send_scratch_command(bcast_str)


def send_scratch_command(cmd):
    global scratch_socket
    length = len(cmd).to_bytes(4, byteorder='big')
    scratch_socket.send(length + cmd.encode("utf-8"))


def create_socket(host, port):
    try:
        scratch_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scratch_sock.connect((host, port))
    except socket.error:
        print("There was an error connecting to Scratch!")
        print("Could not find MESH session at %s:%s" % (host, port))
        sys.exit(1)

    return scratch_sock

if __name__ == '__main__':
    # has the hostname been given?
    host = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_HOST

    # setup the socket
    print('Connecting...', end=" ")
    global scratch_socket
    scratch_socket = create_socket(host, PORT)
    print('Connected.')

    scratch_socket.settimeout(SOCKET_TIMEOUT)

    pfd = pfio.PiFaceDigital()

    # hook each input to the callback function
    #ifm = pifacecommon.InputFunctionMap()
    inputlistener = pfio.InputEventListener(chip=pfd)
    for i in range(len(SCRATCH_SENSOR_NAME_INPUT)):
        inputlistener.register(i, pfio.IODIR_BOTH, input_handler)
        broadcast_pin_update(i, 0)  # make scratch aware of the input pins

    scratchlistener = ScratchListener()
    scratchlistener.start()

    try:
        inputlistener.activate()
    except KeyboardInterrupt:
        print("kb int")

    print("ending main thread")

    # print("Stopping...", end=" ")
    # scratchlistener.stop()
    # scratchlistener.join()
    # pfio.deinit()
    # print("Done.")
