import csv
import os
import librosa
import numpy as np
import time
import matplotlib.pylab as plt
import pandas as pd
import json

french_ds = os.listdir('dataset/Fr')

'''dico_audio_note = {}

with open('./dataset/Fr_annotate.csv', newline='') as file:
    for i in csv.DictReader(file):
        dico_audio_note[i.get('AUDIO')] = i.get('NOTE')'''


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def exist(file):
    return os.path.isfile(file)


def get_tempo(file):
    if exist(file):
        y, sr = librosa.load(file)
        onset_env = librosa.onset.onset_strength(y=y, sr=sr)
        tempo = librosa.feature.tempo(onset_envelope=onset_env, sr=sr)
        return int(tempo)


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
        return int(abs(librosa.power_to_db(S ** 2).mean()))
    else:
        print(file)


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


def write_feature_info(file_dest, dico):
    try:
        file_dest = open(file_dest, "w")
        for audio in dico:
            file_dest.write(
                str(audio) +
                " -> " +
                "NOTE: " + str(dico.get(audio)) + " " +
                "DB: " + str(get_db('dataset/Fr/' + str(audio) + ".mp3")) + " " +
                "TEMPO: " + str(get_tempo('dataset/Fr/' + str(audio) + ".mp3")) + "\n"
            )

    except ValueError:
        print("error")

    file_dest.close()


def extract_csv_to_dico(dico_path):
    dico_audio_note = {}
    with open(dico_path, newline='') as file:
        for i in csv.DictReader(file):
            dico_audio_note[i.get('AUDIO')] = i.get('NOTE')
    return dico_audio_note


def extract_db_vector(txt_path_file):
    dbs = []
    with open(txt_path_file) as file:
        for row in file.readlines():
            audio_info = row.split("->")[1]
            if audio_info.split("DB: ")[1][0] != 'N':
                dbs.append(int(audio_info.split("DB: ")[1][0] + audio_info.split("DB: ")[1][1]))
            else:
                dbs.append("null")
    return dbs


def extract_tempo_vector(txt_path_file):
    tempos = []
    with open(txt_path_file) as file:
        for row in file.readlines():
            audio_info = row.split("->")[1]
            tempos.append(
                audio_info.split("TEMPO: ")[1][0] + \
                audio_info.split("TEMPO: ")[1][1] + \
                audio_info.split("TEMPO: ")[1][2])
    return tempos


def extract_notation_vector(txt_path_file):
    vectors = []
    with open(txt_path_file) as file:
        for row in file.readlines():
            audio_info = row.split("->")[1]
            vectors.append(audio_info.split("NOTE: ")[1][0])
    return vectors

def main():
    start = time.time()

    dico = extract_csv_to_dico("./dataset/Fr_annotate.csv")
    write_feature_info("./evaluation/Fr_features", dico)
    #print(extract_notation_vector("./evaluation/Fr_features"))

    end = time.time()
    print("Time: " + str(end - start))


main()