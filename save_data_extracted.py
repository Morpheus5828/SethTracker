import csv
import extract_feature as ef


def write_feature_info(file_dest, dico):
    try:
        with open(file_dest, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["id", "grade", "rate", "time", "intensity"])
            for audio in dico.keys():
                array_info = [
                    audio,
                    dico.get(audio),
                    ef.get_rate('dataset/Fr/' + str(audio) + ".mp3"),
                    ef.get_audio_time('dataset/Fr/' + str(audio) + ".mp3"),
                    ef.get_intensity('dataset/Fr/' + str(audio) + ".mp3")
                ]

                writer.writerow(array_info)
        file.close()

    except ValueError:
        print("error")


def convert_csv_to_dico(dico_path):
    dico_audio_note = {}
    with open(dico_path, newline='') as file:
        for i in csv.DictReader(file):
            dico_audio_note[i.get('AUDIO')] = i.get('NOTE')
    return dico_audio_note


write_feature_info("evaluation/Fr_features", convert_csv_to_dico("dataset/Fr_annotate.csv"))
