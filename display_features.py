import math

import librosa
from scipy.io import wavfile
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import os

import extract_audio_information
import extract_feature as ef
import numpy as np

french_ds = os.listdir('dataset/Fr')


class Point:
    def __init__(self, db, tempo, note):
        self.db = db
        self.tempo = tempo
        self.note = note


def extract_records_gradation(limit):
    feature_path = "./evaluation/Fr_features"
    note = ef.extract_grade_vector(feature_path)
    list_id_under_limit = []
    note_id_under_limit = []
    list_id_overhead_limit = []
    note_id_overhead_limit = []
    counter = 0
    for index in range(len(note)):
        if note[index] != ' ':
            if int(note[index]) >= limit:
                counter += 1
                note_id_overhead_limit.append(int(note[index]))
                list_id_overhead_limit.append(index)
            else:
                note_id_under_limit.append(int(note[index]))
                list_id_under_limit.append(index)

    '''print(
        str(len(list_id_overhead_limit)),
        " on ",
        str(len(list_id_under_limit) + len(list_id_overhead_limit)),
        " overhead the limit"
    )'''
    return list_id_under_limit, note_id_under_limit, list_id_overhead_limit, note_id_overhead_limit


def display_records_gradation(limit):
    plt.xlim(0, 461)
    plt.ylim(0, 10)
    list_id_under_limit, note_id_under_limit, list_id_overhead_limit, note_id_overhead_limit = extract_records_gradation(
        limit)
    plt.scatter(list_id_under_limit, note_id_under_limit)
    plt.scatter(list_id_overhead_limit, note_id_overhead_limit)

    plt.axhline(y=limit, label='Agression Limit: ' + str(limit))
    plt.xlabel('Record id')
    plt.ylabel('Grade')

    plt.legend()
    plt.title('Records gradation')
    return list_id_under_limit, list_id_overhead_limit


def display_intensity_by_rate(feature_path, list_id, title, xmax, ymax):
    plt.figure(title)
    rate = ef.extract_rate_vector(feature_path)
    intenisty = ef.extract_intensity_vector(feature_path)
    grade = ef.extract_grade_vector(feature_path)

    '''list_point = []

    rate = np.array(rate)
    intenisty = np.array(intenisty)
    grade = np.array(grade)

    for i in range(len(rate)):
        list_point.append([rate[i], intenisty[i]])


    model = LinearRegression()
    model.fit(list_point, grade)
    print(model.score(list_point, grade))'''
    # plt.scatter(list_point, b)

    '''plt.xlim(0, xmax)
    plt.ylim(0, ymax)
    plt.title(title)'''
    # plt.plot(a, model.predict(a), c="r")

    plt.xlabel('Rate in beat per minute')
    plt.ylabel('Intensity in dB')


def display_intensity_freq_rate(feature_path, list_id_under, list_id_over):
    plt.figure()
    a = ef.extract_sample_rate(feature_path, list_id_under)
    b = ef.extract_sample_intensity(feature_path, list_id_under)
    c = ef.extract_sample_freq(feature_path, list_id_under)

    d = ef.extract_sample_rate(feature_path, list_id_over)
    e = ef.extract_sample_intensity(feature_path, list_id_over)
    f = ef.extract_sample_freq(feature_path, list_id_over)

    ax = plt.axes(projection='3d')
    ax.scatter(a, b, c, 'blue')
    ax.scatter(d, e, f, 'red')


def display_audiogram(file):
    y, sr = librosa.load(file)
    fig, ax = plt.subplots()
    D = librosa.stft(y)  # STFT of y
    S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)
    img = librosa.display.specshow(S_db, x_axis='time', y_axis='log', ax=ax)
    ax.set(title='H.13.mp3 Audiogram ')
    fig.colorbar(img, ax=ax, format="%+2.f dB")
    plt.show()


def display_sonogram(file):
    y, sr = extract_audio_information.get_file_load_setting(file)
    time = np.arange(0, len(y)) / sr
    fig, ax = plt.subplots()
    ax.plot(time, y)
    ax.set_xlabel("Time in Second (s)")
    ax.set_ylabel("Sound pressure in Pascal (Pa)")
    ax.set_title(file + "Sonogram")
    plt.show()


def pascal_to_db(p) -> float:
    try:
        print(p)
        return 20 * math.log10(abs(p) / 0.00002)
    except:
        print("pb: " + str(p))
        return 0


def date_to_freq(d):
    if d == 0:
        return d
    return 1 / d


def main():
    # dico = ef.convert_csv_to_dico("./dataset/Fr_annotate.csv")
    # ef.write_feature_info("./evaluation/Fr_features", dico)

    display_audiogram("dataset/Fr/H.13.mp3")

    feature_path = "./evaluation/Fr_features"

    # rate = ef.extract_rate_vector(feature_path)
    # note = ef.extract_notation_vector(feature_path)
    # tempo = ef.extract_tempo_vector(feature_path)

    '''list_id_under_limit, note_id_under_limit, list_id_overhead_limit, note_id_overhead_limit = extract_records_gradation(
        6)'''

    # display_records_gradation(6)

    # display_intensity_by_rate(feature_path, list_id_under_limit, "Record under limit", 300, 60)

    # display_intensity_by_rate(feature_path, list_id_overhead_limit, "Record overhead limit", 300, 60)

    # display_intensity_freq_rate(feature_path, list_id_under_limit, list_id_overhead_limit)

    # plt.show()


main()
