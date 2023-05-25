import csv
import os
import librosa
import numpy as np
import time
import matplotlib.pylab as plt
import pandas as pd
import json

french_ds = os.listdir('dataset/Fr')

dico_audio_note = {}

with open('./dataset/Fr_annotate.csv', newline='') as file:
    for i in csv.DictReader(file):
        dico_audio_note[i.get('AUDIO')] = i.get('NOTE')


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def exist(file):
    return os.path.isfile(file)


################################################

def get_rate(file):
    if exist(file):
        y, sr = librosa.load(file)
        onset_env = librosa.onset.onset_strength(y=y, sr=sr)
        tempo = librosa.feature.tempo(onset_envelope=onset_env, sr=sr)
        return int(tempo)


def get_freq_average(file):
    if exist(file):
        y, sr = librosa.load(file)
        S = np.abs(librosa.stft(y))
        chroma = librosa.feature.chroma_stft(S=S, sr=sr)
        chroma = np.average(chroma)
        return str(chroma)


def get_intensity(file):
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


################################################

def write_feature_info(file_dest, dico):
    try:
        file_dest = open(file_dest, "w")
        for audio in dico:
            file_dest.write(
                str(audio) +
                " -> " +
                "GRADE: " + str(dico.get(audio)) + " " +
                "RATE: " + str(get_rate('dataset/Fr/' + str(audio) + ".mp3")) + " " +
                "FREQ: " + str(get_freq_average('dataset/Fr/' + str(audio) + ".mp3")) + " " +
                "INTENSITY: " + str(get_intensity('dataset/Fr/' + str(audio) + ".mp3")) + " " + "\n"
            )

    except ValueError:
        print("error")

    file_dest.close()


def convert_csv_to_dico(dico_path):
    dico_audio_note = {}
    with open(dico_path, newline='') as file:
        for i in csv.DictReader(file):
            dico_audio_note[i.get('AUDIO')] = i.get('NOTE')
    return dico_audio_note


################################################

def extract_rate_vector(txt_path_file):
    dbs = []
    with open(txt_path_file) as file:
        for row in file.readlines():
            audio_info = row.split("->")[1]
            if audio_info.split("RATE: ")[1][0] != 'N':
                dbs.append(
                    audio_info.split("RATE: ")[1][0] +
                    audio_info.split("RATE: ")[1][1] +
                    audio_info.split("RATE: ")[1][2]
                )
            else:
                dbs.append("null")
    return dbs


def extract_freq_vector(txt_path_file):
    freqs = []
    with open(txt_path_file) as file:
        for row in file.readlines():
            audio_info = row.split("->")[1]
            if audio_info.split("FREQ: ")[1][0] != "N":
                freqs.append(
                    float(
                        (audio_info.split("FREQ: ")[1][0]) +
                        (audio_info.split("FREQ: ")[1][1]) +
                        (audio_info.split("FREQ: ")[1][2]) +
                        (audio_info.split("FREQ: ")[1][3]) +
                        (audio_info.split("FREQ: ")[1][4])
                    )
                )

    return freqs


def extract_intensity_vector(txt_path_file):
    intensity = []
    with open(txt_path_file) as file:
        for row in file.readlines():
            audio_info = row.split("->")[1]
            if audio_info.split("INTENSITY: ")[1][0] != 'N':
                intensity.append(
                    int(
                        audio_info.split("INTENSITY: ")[1][0] +
                        audio_info.split("INTENSITY: ")[1][1]
                    )
                )
    return intensity


def extract_grade_vector(txt_path_file):
    vectors = []
    with open(txt_path_file) as file:
        for row in file.readlines():
            audio_info = row.split("->")[1]
            if audio_info.split("GRADE: ")[1][1] == str(0):
                vectors.append(10)
            else:
                vectors.append(audio_info.split("GRADE: ")[1][0])
    return vectors


################################################

def extract_sample_rate(txt_path_file, list_id):
    sample_dbs = []
    rate = extract_rate_vector(txt_path_file)
    for i in list_id:
        sample_dbs.append(int(rate[i]))
    return sample_dbs


def extract_sample_freq(txt_path_file, list_id):
    sample_freq = []
    freqs = extract_freq_vector(txt_path_file)
    for i in list_id:
        sample_freq.append(freqs[i])
    return sample_freq


def extract_sample_intensity(txt_path_file, list_id):
    sample = []
    intensities = extract_intensity_vector(txt_path_file)
    for i in list_id:
        sample.append(intensities[i])
    return sample


################################################
def main():
    start = time.time()

    # write_feature_info("evaluation/Fr_features", dico_audio_note)


    end = time.time()
    print("Time: " + str(end - start))


main()
