# -*- coding: UTF-8 -*-

from os import mkfifo, stat
from os.path import exists
from stat import S_ISFIFO


def isfifo(path):
    if exists(path):
        return S_ISFIFO(stat(path).st_mode)
    return False


def openfifo(path, mode):
    if not isfifo(path):
        mkfifo(path)
    return open(path, mode)


class FIFO():
    def __init__(self, path='fifo'):
        self.path = path


    def write(self, text):
        fifo = openfifo(self.path, 'w')
        fifo.write(text)
        fifo.close()

    def read(self):
        fifo = openfifo(self.path, 'rb')
        text = fifo.read()
        fifo.close()
        return text

