import os
import struct

import numpy as np


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def exist(file):
    return os.path.isfile(file)


def str_to_np_array(array):
    array = array.strip('][').split(',')
    result = []
    sorted(array, reverse=True)
    for rate in range(min(3, len(array)-1), 0, -1):
        result.append(abs(float(array[rate])))

    return np.array(result)


def concatenate_array(array_one, array_two):
    return np.concatenate((str_to_np_array(array_one), str_to_np_array(array_two)), dtype=float)


def array_to_bin(rate_array):
    array = rate_array.strip('][').split(',')
    result = ""
    for rate in array:
        result += str(float_to_bin(rate)) + "0"
    return result


def float_to_bin(number):
    return ''.join('{:08b}'.format(b) for b in struct.pack('>f', float(number)))