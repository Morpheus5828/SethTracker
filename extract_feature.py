import csv
import os
import librosa
import numpy as np
import time
import matplotlib.pylab as plt
import pandas as pd

french_ds = os.listdir('dataset/Fr')
french_ds_features = open('evaluation/Fr_features', 'w')

dico_audio_note = {}

with open('./dataset/Fr_annotate.csv', newline='') as file:
    for i in csv.DictReader(file):
        dico_audio_note[i.get('AUDIO')] = i.get('NOTE')


def exist(file):
    return os.path.isfile(file)


def get_tempo(file):
    if exist(file):
        y, sr = librosa.load(file)
        onset_env = librosa.onset.onset_strength(y=y, sr=sr)
        tempo = librosa.feature.tempo(onset_envelope=onset_env, sr=sr)
        return str(tempo)


def get_freq_average(file):
    y, sr = librosa.load(file)
    S = np.abs(librosa.stft(y))
    chroma = librosa.feature.chroma_stft(S=S, sr=sr)
    chroma = np.average(chroma)
    return str(chroma)


def get_db(file):
    if exist(file):
        y, sr = librosa.load(file)
        S = np.abs(librosa.stft(y))
        return librosa.power_to_db(S ** 2).mean()


def get_wave(file):
    try:
        y, sr = librosa.load(file, duration=10)
        fig, ax = plt.subplots(nrows=1, sharex=True)
        ax.set(xlim=[0, 7], title='Wave', ylim=[-0.5, 0.5])
        librosa.display.waveshow(y, sr=12000, ax=ax, max_points=1000)
        ax.label_outer()
        return y
    except:
        return None


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def get_plot_from_wave(wave):
    positive_list = []
    negative_list = []
    list_point = []
    print(len(wave))
    # create list_point of all wave points
    try:
        for i in range(len(wave) - 1):
            if i % 2 == 0:
                list_point.append(Point(i, wave[i + 1]))
    except ValueError:
        print("Break")

    # order list_point by ordinate
    list_point.sort(key=lambda point: point.y, reverse=True)

    for i in range(10):
        positive_list.append(list_point[i])

    list_x = []
    list_y = []
    for j in positive_list:
        list_x.append(j.x)
        list_y.append(j.y)

    print(list_x)
    print(list_y)

    plt.scatter(list_x, list_y, color="red")
    plt.show()


def get_coef(x1, x2, y1, y2):
    delta_y = y2 - y1
    delta_x = x2 - x1
    if delta_x != 0:
        return delta_y / delta_x


def main():
    start = time.time()

    try:
        for audio in dico_audio_note:
            french_ds_features.write(
                str(audio) +
                " -> " +
                "NOTE: " + str(dico_audio_note.get(audio)) + " " +
                "DB: " + str(get_db('dataset/Fr/' + audio + ".mp3")) + " " +
                "TEMPO: " + str(get_tempo('dataset/Fr/' + audio + ".mp3")) + "\n"
            )

    except ValueError:
        print("error")

    french_ds_features.close()

    end = time.time()
    print("Time: " + str(end - start))


main()
