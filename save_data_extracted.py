import csv

import extract_audio_information
import extract_feature as ef
import numpy as np
from scipy.fft import fft, ifft


def write_feature_info(file_dest, dico):
    try:
        with open(file_dest, 'w', newline='') as file:
            writer = csv.writer(file)
            row = ["id", "grade"]
            for i in range(1, 175276):
                row.append(str(i))
            writer.writerow(row)
            # max 1616425
            c = 0
            for audio in dico.keys():
                if c == 30:
                    file.close()
                    return
                array_info = [
                    audio,
                    dico.get(audio),
                    create_tab_for_tf('dataset/Fr/' + audio + ".mp3")
                    # get_average_of_ten_max_value(ef.get_rate('dataset/Fr/' + str(audio) + ".mp3")),
                    # ef.get_audio_time('dataset/Fr/' + str(audio) + ".mp3"),
                    # get_average_of_ten_max_value(ef.get_intensity('dataset/Fr/' + str(audio) + ".mp3")),
                    # get_average_of_ten_max_value(ef.get_freq('dataset/Fr/' + str(audio) + ".mp3"))
                ]
                c += 1
            writer.writerow(array_info)

        file.close()

    except ValueError:
        print("error")


def create_tab_for_tf(file):
    tab = ef.get_fourier_transform(file)

    result = ''
    c = 0
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if i == len(tab) - 1 and j == len(tab[i]) - 1:
                result += (str(tab[i][j]))
                c += 1
            else:
                result += (str(tab[i][j]) + ",")
                c += 1
    zero_size_tab = 1616425 - c
    for i in range(zero_size_tab):
        result += "0,"

    return result


def convert_csv_to_dico(dico_path):
    dico_audio_note = {}
    with open(dico_path, newline='') as file:
        for i in csv.DictReader(file):
            dico_audio_note[i.get('AUDIO')] = i.get('NOTE')
    return dico_audio_note


# 307500

def get_average_of_ten_max_value(array):
    ten_max_value = []
    sorted(array, reverse=True)
    for index in range(5):
        ten_max_value.append(abs(array[index]))
    return np.array(ten_max_value).mean()


# create_tab_for_tf("dataset/Fr/F.27.mp3")
write_feature_info("evaluation/Fr_features", convert_csv_to_dico("dataset/Fr_annotate.csv"))
