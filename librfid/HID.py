# -*- coding: UTF-8 -*-

from evdev import ecodes, categorize
from Scancodes import SCANCODES

# Key Down event is 1
KEY_DOWN = 1

def get_keydown(event):
    key = None
    if event.type == ecodes.EV_KEY:
        data = categorize(event)
        if data.keystate == KEY_DOWN:
            key = SCANCODES[data.scancode] or 'UNKNOWN'
    return key
