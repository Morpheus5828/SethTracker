import os


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def exist(file):
    return os.path.isfile(file)
