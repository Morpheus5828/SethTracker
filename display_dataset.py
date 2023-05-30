import librosa
import matplotlib.pyplot as plt
import os

from sklearn.linear_model import LinearRegression

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
    #plt.scatter(list_point, b)


    '''plt.xlim(0, xmax)
    plt.ylim(0, ymax)
    plt.title(title)'''
    #plt.plot(a, model.predict(a), c="r")

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


def display_frequency_by_time(file):
    fig, ax = plt.subplots()
    tg = ef.get_tempogram(file)
    dtempo = ef.get_freq_average(file)
    librosa.display.specshow(tg, x_axis='time', y_axis='tempo', ax=ax)
    ax.plot(librosa.times_like(dtempo), dtempo, color='c', linewidth=1.5, label='Tempo')
    ax.set(title='Dynamic tempo estimation')
    plt.xlabel('Time (in seconds)')
    plt.ylabel('Beats per minute')
    ax.legend()
    plt.savefig(file + ".png", dpi=300)


def main():
    # dico = ef.convert_csv_to_dico("./dataset/Fr_annotate.csv")
    # ef.write_feature_info("./evaluation/Fr_features", dico)

    feature_path = "./evaluation/Fr_features"

    # rate = ef.extract_rate_vector(feature_path)
    # note = ef.extract_notation_vector(feature_path)
    # tempo = ef.extract_tempo_vector(feature_path)

    list_id_under_limit, note_id_under_limit, list_id_overhead_limit, note_id_overhead_limit = extract_records_gradation(
        6)

    # display_records_gradation(6)

    display_intensity_by_rate(feature_path, list_id_under_limit, "Record under limit", 300, 60)

    # display_intensity_by_rate(feature_path, list_id_overhead_limit, "Record overhead limit", 300, 60)

    # display_intensity_freq_rate(feature_path, list_id_under_limit, list_id_overhead_limit)


    # plt.show()


main()
