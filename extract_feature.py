import csv
import os
import librosa
import numpy as np
import pandas as pd
import time
import matplotlib.pylab as plt
import extract_audio_information as eai
from sklearn.linear_model import LinearRegression


# rate beat per minute https://librosa.org/doc/main/generated/librosa.feature.tempo.html
def get_rate(file):
    y, sr = eai.get_file_load_setting(file)
    onset_env = librosa.onset.onset_strength(y=y, sr=sr)
    return librosa.feature.tempo(onset_envelope=onset_env, sr=sr, aggregate=None)


# time in second
def get_audio_time(file):
    y, sr = eai.get_file_load_setting(file)
    return round(librosa.get_duration(y=y, sr=sr, n_fft=512), 2)


# intensity in decibel (dB) https://librosa.org/doc/main/generated/librosa.stft.html
def get_intensity(file):
    y, sr = eai.get_file_load_setting(file)
    magnitude_freq = np.abs(librosa.stft(y, n_fft=512))  # 512 for voice management
    return np.array(librosa.power_to_db(magnitude_freq ** 2))


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

    a = extract_rate_vector("evaluation/Fr_features")
    b = extract_intensity_vector("evaluation/Fr_features")
    print(a[0])
    '''x = []
    for i in range(len(a)):
        x.append([float(a[i]), float(b[i])])

    label = extract_grade_vector("evaluation/Fr_features")

    model = LinearRegression()
    model.fit(x, label)'''
    #print(model.score(list_point, grade))


    end = time.time()
    print("Time: " + str(end - start))

main()
