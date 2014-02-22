#! /usr/bin/env python
# -*- coding: UTF-8 -*-

from evdev import InputDevice
from librfid.HID import get_keydown
from librfid.Timer import Timer

# Setup Input Device
dev = InputDevice('/dev/input/event2')

# Setup ID Buffer
BUFFER_SIZE = 5
id_buffer = []

# Setup Timer
TIMEOUT = 5.0
timer = Timer(timeout=TIMEOUT)

# Read Inpud Device Forever
for event in dev.read_loop():
    # Check Timer. Clear Buffer if timed out
    if timer.timedout():
        print "Timeout"
        id_buffer = []

    # Get key down event
    key = get_keydown(event)
    # Keep going if key is None
    if not key:
        continue

    # Add Key to Buffer
    id_buffer.append(key)
    buf_len = len(id_buffer)

    # If we got our first character, start the timer
    if buf_len == 1:
        timer.start()

    # If Buffer is full. Print and reset buffer
    if buf_len == BUFFER_SIZE:
        print "Buffer: %s" % ''.join(id_buffer)
        id_buffer = []
        timer.clear()
