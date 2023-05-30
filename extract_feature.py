import csv
import os
import librosa
import numpy as np
import time
import matplotlib.pylab as plt
import extract_audio_information as eai


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
    magnitude_freq = np.abs(librosa.stft(y, n_fft=512)) # 512 for voice management
    return np.array(librosa.power_to_db(magnitude_freq ** 2))


def get_tempogram(file):
    y, sr = eai.get_file_load_setting(file)
    onset_env = librosa.onset.onset_strength(y=y, sr=sr)
    return librosa.feature.tempogram(onset_envelope=onset_env, sr=sr, hop_length=512)


################################################


def extract_rate_vector(txt_path_file):
    dbs = []
    with open(txt_path_file) as file:
        for row in file.readlines():
            audio_info = row.split("->")[1]
            if audio_info.split("RATE: ")[1][0] != '-':
                dbs.append(
                    int(
                        audio_info.split("RATE: ")[1][0] +
                        audio_info.split("RATE: ")[1][1] +
                        audio_info.split("RATE: ")[1][2]
                    )
                )
    return np.array(dbs)


def extract_intensity_vector(txt_path_file):
    intensity = []
    with open(txt_path_file) as file:
        for row in file.readlines():
            audio_info = row.split("->")[1]
            if audio_info.split("INTENSITY: ")[1][0] != '-':
                intensity.append(
                    int(
                        audio_info.split("INTENSITY: ")[1][0] +
                        audio_info.split("INTENSITY: ")[1][1]
                    )
                )
    return np.array(intensity)


def extract_grade_vector(txt_path_file):
    grades = []
    with open(txt_path_file) as file:
        for row in file.readlines():
            audio_info = row.split("->")[1]
            if audio_info.split("GRADE: ")[1][0] != ' ':
                if audio_info.split("GRADE: ")[1][1] == str(0):
                    grades.append(10)
                else:
                    grades.append(int(audio_info.split("GRADE: ")[1][0]))

    return np.array(grades)


################################################

'''def extract_sample_rate(txt_path_file, list_id):
    sample_dbs = []
    dbs = []
    with open(txt_path_file) as file:
        for index in list_id:
            for row in file.readlines():
                audio_info = row.split("->")[1]
                if audio_info.split("RATE: ")[1][0] != '-':
                    dbs.append(
                        int(
                            audio_info.split("RATE: ")[1][0] +
                            audio_info.split("RATE: ")[1][1] +
                            audio_info.split("RATE: ")[1][2]
                        )
                    )
    return np.array(dbs)
    return sample_dbs


def extract_sample_intensity(txt_path_file, list_id):
    sample = []
    intensities = extract_intensity_vector(txt_path_file)
    for i in list_id:
        sample.append(intensities[i])
    return sample


def extract_sample_grade(txt_path_file, list_id):'''

################################################
def main():
    start = time.time()

    # write_feature_info("evaluation/Fr_features", dico_audio_note)
    # get_freq_average("dataset/Fr/" + french_ds[0])
    end = time.time()
    print("Time: " + str(end - start))

# main()
