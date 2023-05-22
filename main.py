import pandas as pd
import csv

# 1. extract all rows from csv file
dico_audio_note = {}

with open('./dataset/Fr_annotate.csv', newline='') as file:
    for i in csv.DictReader(file):
        dico_audio_note[i.get('AUDIO')] = i.get('NOTE')

        



