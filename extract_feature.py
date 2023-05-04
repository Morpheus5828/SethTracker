import os
import statistics

import librosa
import numpy as np
import time
import matplotlib.pylab as plt

colere_dataset = os.listdir("dataset/CaFE_192k_1_/Colère")
degout_dataset = os.listdir("dataset/CaFE_192k_1_/Dégoût")
joie_dataset = os.listdir("dataset/CaFE_192k_1_/Joie")
neutre_dataset = os.listdir("dataset/CaFE_192k_1_/Neutre")
peur_dataset = os.listdir("dataset/CaFE_192k_1_/Peur")
surprise_dataset = os.listdir("dataset/CaFE_192k_1_/Surprise")
tristesse_dataset = os.listdir("dataset/CaFE_192k_1_/Tristesse")


colere_feature_result = open("evaluation/colere_feature_result.txt", "w")
degout_feature_result = open("evaluation/degout_feature_result.txt", "w")
joie_feature_result = open("evaluation/joie_feature_result.txt", "w")
neutre_feature_result = open("evaluation/neutre_feature_result.txt", "w")
peur_feature_result = open("evaluation/peur_feature_result.txt", "w")
surprise_feature_result = open("evaluation/surprise_feature_result.txt", "w")
tristesse_feature_result = open("evaluation/tristesse_feature_result.txt", "w")


def get_tempo(file):
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
    y, sr = librosa.load(file)
    S = np.abs(librosa.stft(y))
    return librosa.power_to_db(S**2).mean()


def get_wave(file):
    y, sr = librosa.load(file, duration=10)
    fig, ax = plt.subplots(nrows=1, sharex=True)
    ax.set(xlim=[0.75, 5], title='Wave', ylim=[-1, 1])
    librosa.display.waveshow(y, sr=sr, ax=ax, marker='.', label='Full signal')
    ax.label_outer()
    plt.show()




def main():
    start = time.time()
    ########################### Colere

    '''colere_feature_result.write("--> Colere Faible\n")

    colere_list_faible = os.listdir("dataset/CaFE_192k_1_/Colère/" + colere_dataset[0])
    colere_list_forte = os.listdir("dataset/CaFE_192k_1_/Colère/" + colere_dataset[1])

    for file in colere_list_faible:
        file = "dataset/CaFE_192k_1_/Colère/Faible/" + file
        colere_feature_result.write("\t" + file + " , Tempo:" + str(get_tempo(file)) + " , DB: " + str(get_db(file)) + "\n")

    colere_feature_result.write("--> Colere Forte\n")

    for file in colere_list_forte:
        file = "dataset/CaFE_192k_1_/Colère/Fort/" + file
        colere_feature_result.write("\t" + file + " , Tempo:" + str(get_tempo(file)) + " , DB: " + str(get_db(file)) + "\n")

    colere_feature_result.close()'''

    ########################### Degout

    '''degout_feature_result.write("--> Degout Faible\n")

    degout_list_faible = os.listdir("dataset/CaFE_192k_1_/Dégoût/" + colere_dataset[0])
    degout_list_forte = os.listdir("dataset/CaFE_192k_1_/Dégoût/" + colere_dataset[1])

    for file in degout_list_faible:
        file = "dataset/CaFE_192k_1_/Dégoût/Faible/" + file
        degout_feature_result.write("\t" + file + " , Tempo:" + str(get_tempo(file)) + " , DB: " + str(get_db(file)) + "\n")

    degout_feature_result.write("--> Degout Forte\n")

    for file in degout_list_forte:
        file = "dataset/CaFE_192k_1_/Dégoût/Fort/" + file
        degout_feature_result.write("\t" + file + " , Tempo:" + str(get_tempo(file)) + " , DB: " + str(get_db(file)) + "\n")

    degout_feature_result.close()'''

    ########################### Joie

    '''joie_feature_result.write("--> Joie Faible\n")

    joie_list_faible = os.listdir("dataset/CaFE_192k_1_/Joie/" + colere_dataset[0])
    joie_list_forte = os.listdir("dataset/CaFE_192k_1_/Joie/" + colere_dataset[1])

    for file in joie_list_faible:
        file = "dataset/CaFE_192k_1_/Joie/Faible/" + file
        joie_feature_result.write(
            "\t" + file + " , Tempo:" + str(get_tempo(file)) + " , DB: " + str(get_db(file)) + "\n")

    joie_feature_result.write("--> Joie Forte\n")

    for file in joie_list_forte:
        file = "dataset/CaFE_192k_1_/Joie/Fort/" + file
        joie_feature_result.write(
            "\t" + file + " , Tempo:" + str(get_tempo(file)) + " , DB: " + str(get_db(file)) + "\n")

    joie_feature_result.close()'''

    ########################### Neutre

    '''for file in neutre_dataset:
        file = "dataset/CaFE_192k_1_/Neutre/" + file
        neutre_feature_result.write(
            "\t" + file + " , Tempo:" + str(get_tempo(file)) + " , DB: " + str(get_db(file)) + "\n")

    neutre_feature_result.close()'''

    ########################### Peur

    '''peur_feature_result.write("--> Peur Faible\n")

    peur_list_faible = os.listdir("dataset/CaFE_192k_1_/Peur/" + colere_dataset[0])
    peur_list_forte = os.listdir("dataset/CaFE_192k_1_/Peur/" + colere_dataset[1])

    for file in peur_list_faible:
        file = "dataset/CaFE_192k_1_/Peur/Faible/" + file
        peur_feature_result.write(
            "\t" + file + " , Tempo:" + str(get_tempo(file)) + " , DB: " + str(get_db(file)) + "\n")

    peur_feature_result.write("--> Peur Forte\n")

    for file in peur_list_forte:
        file = "dataset/CaFE_192k_1_/Peur/Fort/" + file
        peur_feature_result.write(
            "\t" + file + " , Tempo:" + str(get_tempo(file)) + " , DB: " + str(get_db(file)) + "\n")

    peur_feature_result.close()'''

    ########################### Surprise

    '''surprise_feature_result.write("--> Surprise Faible\n")

    surprise_list_faible = os.listdir("dataset/CaFE_192k_1_/Surprise/" + colere_dataset[0])
    surprise_list_forte = os.listdir("dataset/CaFE_192k_1_/Surprise/" + colere_dataset[1])

    for file in surprise_list_faible:
        file = "dataset/CaFE_192k_1_/Surprise/Faible/" + file
        surprise_feature_result.write(
            "\t" + file + " , Tempo:" + str(get_tempo(file)) + " , DB: " + str(get_db(file)) + "\n")

    surprise_feature_result.write("--> Surprise Forte\n")

    for file in surprise_list_forte:
        file = "dataset/CaFE_192k_1_/Surprise/Fort/" + file
        surprise_feature_result.write(
            "\t" + file + " , Tempo:" + str(get_tempo(file)) + " , DB: " + str(get_db(file)) + "\n")

    surprise_feature_result.close()'''

    ########################### Tristesse

    '''tristesse_feature_result.write("--> Tristesse Faible\n")

    tristesse_list_faible = os.listdir("dataset/CaFE_192k_1_/Tristesse/" + colere_dataset[0])
    tristesse_list_forte = os.listdir("dataset/CaFE_192k_1_/Tristesse/" + colere_dataset[1])

    for file in tristesse_list_faible:
        file = "dataset/CaFE_192k_1_/Tristesse/Faible/" + file
        tristesse_feature_result.write(
            "\t" + file + " , Tempo:" + str(get_tempo(file)) + " , DB: " + str(get_db(file)) + "\n")

    tristesse_feature_result.write("--> Tristesse Forte\n")

    for file in tristesse_list_forte:
        file = "dataset/CaFE_192k_1_/Tristesse/Fort/" + file
        tristesse_feature_result.write(
            "\t" + file + " , Tempo:" + str(get_tempo(file)) + " , DB: " + str(get_db(file)) + "\n")

    tristesse_feature_result.close()'''
    get_wave("dataset/CaFE_192k_1_/Colère/Fort/01-C-2-1.aiff")
    end = time.time()
    print("Time: " + str(end-start))


main()

