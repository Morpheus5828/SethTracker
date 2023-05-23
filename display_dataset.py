import matplotlib.pyplot as plt
import extract_feature as ef


def main():
    dico = ef.extract_csv_to_dico("./dataset/Fr_annotate.csv")
    ef.write_feature_info("./evaluation/Fr_features", dico)
    feature_path = "./evaluation/Fr_features"
    db = ef.extract_db_vector(feature_path)
    note = ef.extract_notation_vector(feature_path)
    #note.remove(' ')

    print(len(note))

    for i in range(len(note)):
        if note[i] != ' ':
            print(db[i])
            #plt.scatter(note[i], db[i], c='red')



    #plt.show()


main()