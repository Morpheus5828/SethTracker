import matplotlib.pyplot as plt
import numpy as np

import extract_feature as ef
import pandas as pd


class Point:
    def __init__(self, db, tempo, note):
        self.db = db
        self.tempo = tempo
        self.note = note


def display_records_gradation(limit):
    plt.xlim(0, 461)
    plt.ylim(0, 10)

    feature_path = "./evaluation/Fr_features"
    note = ef.extract_notation_vector(feature_path)

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

    print(str(len(list_id_overhead_limit)), " on ", str(len(list_id_under_limit) + len(list_id_overhead_limit)), " overhead the limit")

    plt.scatter(list_id_under_limit, note_id_under_limit)
    plt.scatter(list_id_overhead_limit, note_id_overhead_limit)

    plt.axhline(y=limit, label='Agression Limit: ' + str(limit))
    plt.xlabel('Record id')
    plt.ylabel('Grade')

    plt.legend()
    plt.title('Records gradation')
    plt.show()

def main():
    #dico = ef.extract_csv_to_dico("./dataset/Fr_annotate.csv")
    #ef.write_feature_info("./evaluation/Fr_features", dico)

    feature_path = "./evaluation/Fr_features"

    display_records_gradation(6)

    db = ef.extract_db_vector(feature_path)
    note = ef.extract_notation_vector(feature_path)
    tempo = ef.extract_tempo_vector(feature_path)

    '''note_x_plus = []
    tempo_y_plus = []
    note_x_moins = []
    tempo_y_moins = []

    for i in range(len(note)):
        if (db[i] != ' ' and db[i] != 'null') and (tempo[i] != ' ' and tempo[i] != 'null') and note[i] != ' ':
            if int(note[i]) <= 5:
                note_x_moins.append(int(db[i]))
                tempo_y_moins.append(int(tempo[i]))
            else:
                note_x_plus.append(int(db[i]))
                tempo_y_plus.append(int(tempo[i]))

    plt.scatter(note_x_plus, tempo_y_plus, c='red')
    plt.scatter(note_x_moins, tempo_y_moins, c='blue')
    plt.xlabel("Intensité Sonore en dB")
    plt.ylabel("Tempo en BPM")'''


main()
