import csv
import os
import librosa
import numpy as np
import pandas as pd
import time
from scipy.fft import fft

import extract_audio_information
import extract_audio_information as eai
from sklearn.linear_model import LinearRegression

import tools


# rate beat per minute https://librosa.org/doc/main/generated/librosa.feature.tempo.html
def get_rate(file):
    y, sr = eai.get_file_load_setting(file)
    onset_env = librosa.onset.onset_strength(y=y, sr=sr)
    return list(librosa.feature.tempo(onset_envelope=onset_env, sr=sr, aggregate=None))


# rate in Hz
def get_freq(file):
    freq_bpm = get_rate(file)
    result = np.vectorize(bpm_to_hz)
    return result(freq_bpm)


def get_fourier_transform(file):
    y, sr = eai.get_file_load_setting(file)
    S = np.abs(librosa.stft(y))
    return S
    '''hop_length = 512
    oenv = librosa.onset.onset_strength(y=y, sr=sr, hop_length=hop_length)
    tempogram = librosa.feature.fourier_tempogram(onset_envelope=oenv, sr=sr,hop_length=hop_length)
    return tempogram'''


def bpm_to_hz(bpm):
    return bpm / 60


# time in second
def get_audio_time(file):
    y, sr = eai.get_file_load_setting(file)
    return round(librosa.get_duration(y=y, sr=sr, n_fft=512), 2)


# intensity in decibel (dB) https://librosa.org/doc/main/generated/librosa.stft.html
def get_intensity(file):
    y, sr = eai.get_file_load_setting(file)
    magnitude_freq = np.abs(librosa.stft(y, n_fft=512))  # 512 for voice management
    return librosa.power_to_db(magnitude_freq ** 2).flatten().tolist()


def get_tempogram(file):
    y, sr = eai.get_file_load_setting(file)
    onset_env = librosa.onset.onset_strength(y=y, sr=sr)
    return librosa.feature.tempogram(onset_envelope=onset_env, sr=sr, hop_length=512)


################################################


def extract_rate_vector(txt_path_file):
    column = ["id", "grade", "rate", "time", "intensity"]
    df = pd.read_csv(txt_path_file, usecols=column)
    return pd.Series(df.rate).to_numpy()


def extract_intensity_vector(txt_path_file):
    column = ["id", "grade", "rate", "time", "intensity"]
    df = pd.read_csv(txt_path_file, usecols=column)
    return pd.Series(df.intensity).to_numpy()


def extract_grade_vector(txt_path_file):
    column = ["id", "grade", "rate", "time", "intensity"]
    df = pd.read_csv(txt_path_file, usecols=column)
    return pd.Series(df.grade).to_numpy().astype(int)


################################################


def main():
    start = time.time()

    print(len(get_fourier_transform("dataset/Fr/F.27.mp3")))


    end = time.time()
    print("Time: " + str(end - start))


main()
