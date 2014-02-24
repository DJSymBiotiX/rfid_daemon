#! /usr/bin/env python
# -*- coding: UTF-8 -*-

from librfid.FIFO import FIFO
from librfid.Utils import trim_whitespace

# Setup ID Buffer
BUFFER_SIZE = 5
id_buffer = []

# FIFO Info
FIFO_PATH = 'fifo'
fifo = FIFO(FIFO_PATH)

while True:
    # Wait For Text
    RFID = trim_whitespace(fifo.read())
    print "{%s}" % RFID
