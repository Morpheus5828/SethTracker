import os
import tools
import csv

import librosa


# french_ds = os.listdir('dataset/Fr')


def get_file_load_setting(file):
    if tools.exist(file):
        y, sr = librosa.load(file, sr=1000)
        return y, sr
    else:
        return None


