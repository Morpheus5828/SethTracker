import matplotlib.pyplot as plt
import numpy as np

import extract_feature as ef
import pandas as pd


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
    for i in range(1, len(note)):
        if note[i] != ' ':
            if int(note[i]) >= limit:
                counter += 1
                note_id_overhead_limit.append(int(note[i]))
                list_id_overhead_limit.append(i)
            else:
                note_id_under_limit.append(int(note[i]))
                list_id_under_limit.append(i)

    print(str(len(list_id_overhead_limit)), " on ", str(len(list_id_under_limit) + len(list_id_overhead_limit)),
          " overhead the limit")
    return list_id_under_limit, note_id_under_limit, list_id_overhead_limit, note_id_overhead_limit


def display_records_gradation(limit):
    plt.xlim(0, 461)
    plt.ylim(0, 10)
    list_id_under_limit, note_id_under_limit, list_id_overhead_limit, note_id_overhead_limit = extract_records_gradation(limit)
    plt.scatter(list_id_under_limit, note_id_under_limit)
    plt.scatter(list_id_overhead_limit, note_id_overhead_limit)

    plt.axhline(y=limit, label='Agression Limit: ' + str(limit))
    plt.xlabel('Record id')
    plt.ylabel('Grade')

    plt.legend()
    plt.title('Records gradation')
    return list_id_under_limit, list_id_overhead_limit


def display_intensity_by_tempo_rate(feature_path, list_id, title, xmax, ymax):
    plt.figure(title)
    a = ef.extract_sample_rate(feature_path, list_id)
    b = ef.extract_sample_tempo(feature_path, list_id)
    plt.scatter(a, b)
    plt.xlim(0, xmax)
    plt.ylim(0, ymax)
    plt.title(title)
    plt.xlabel('Rate in dB')
    plt.ylabel('Tempo in bpm')


def display_intensity_freq_tempo(feature_path, list_id, title):
    a = ef.extract_sample_rate(feature_path, list_id)
    b = ef.extract_sample_tempo(feature_path, list_id)
    c = ef.extract_sample_freq(feature_path, list_id)
    print(len(a))
    print(len(b))


def main():
    dico = ef.convert_csv_to_dico("./dataset/Fr_annotate.csv")
    ef.write_feature_info("./evaluation/Fr_features", dico)

    feature_path = "./evaluation/Fr_features"

    # rate = ef.extract_rate_vector(feature_path)
    # note = ef.extract_notation_vector(feature_path)
    # tempo = ef.extract_tempo_vector(feature_path)

    '''list_id_under_limit, note_id_under_limit, list_id_overhead_limit, note_id_overhead_limit = extract_records_gradation(6)

    #display_intensity_by_tempo_rate(feature_path, list_id_under_limit, "Record under limit", 50, 300)

    #display_intensity_by_tempo_rate(feature_path, list_id_overhead_limit, "Record overhead limit", 50, 300)

    #display_intensity_freq_tempo(feature_path, list_id_under_limit, "3D")

    c = ef.extract_sample_freq(feature_path, note_id_under_limit)
'''
    plt.show()

main()
