#! /usr/bin/env python
# -*- coding: UTF-8 -*-

from evdev import InputDevice
from librfid.HID import get_keydown
from librfid.Timer import Timer
from librfid.FIFO import FIFO

# Setup Input Device
dev = InputDevice('/dev/input/event0')

# Setup ID Buffer
BUFFER_SIZE = 10
id_buffer = []
EXCLUDE = ['ENTER']

# Setup Timer
TIMEOUT = 0.5
timer = Timer(timeout=TIMEOUT)

# FIFO Info
FIFO_PATH = 'fifo'
fifo = FIFO(FIFO_PATH)

# Read Inpud Device Forever
for event in dev.read_loop():
    # Check Timer. Clear Buffer if timed out
    if timer.timedout():
        print "Timeout: {%s}" % ''.join(id_buffer)
        id_buffer = []

    # Get key down event
    key = get_keydown(event)

    # Keep going if key is None, or if the key exists in the EXCLUDE array
    if not key or key in EXCLUDE:
        continue

    # Add Key to Buffer
    id_buffer.append(key)
    buf_len = len(id_buffer)

    # If we got our first character, start the timer
    if buf_len == 1:
        timer.start()

    # If Buffer is full. Write and reset buffer
    if buf_len == BUFFER_SIZE:
        id_str = ''.join(id_buffer)
        # We can assume that a proper ID starts with 3 0's
        if id_str[0:3] == '000':
            fifo.write(id_str)
        else:
            print "Incorrect ID: {%s}" % id_str

        # Clear
        id_buffer = []
        timer.clear()
