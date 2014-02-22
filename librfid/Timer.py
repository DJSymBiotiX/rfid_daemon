# -*- coding: UTF-8 -*-

import time

class Timer():
    def __init__(self, timeout=5.0):
        self.timeout = timeout
        self.timestart = None


    def start(self):
        self.timestart = time.time()


    def clear(self):
        self.timestart = None


    def timedout(self):
        if self.timestart and (time.time() - self.timestart) > self.timeout:
            return True
        return False


    def delta(self):
        if self.timestart:
            return time.time() - self.timestart
        return -1
