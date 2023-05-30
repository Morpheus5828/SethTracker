from unittest import TestCase
import extract_audio_information as eaf
import os


class Test(TestCase):
    def test_get_file_load_setting(self):
        y_index = 0
        sr_index = 1
        self.assertEqual(2, len(eaf.get_file_load_setting('../dataset/Fr/F.1.mp3')))
        self.assertEqual(87464, len(eaf.get_file_load_setting('../dataset/Fr/F.1.mp3')[y_index]))
        self.assertEqual(174392, len(eaf.get_file_load_setting('../dataset/Fr/F.2.mp3')[y_index]))
        self.assertEqual(22050, eaf.get_file_load_setting('../dataset/Fr/F.1.mp3')[sr_index])
        self.assertEqual(22050, eaf.get_file_load_setting('../dataset/Fr/F.2.mp3')[sr_index])

    def test_convert_csv_to_dico(self):
        audio_length = 576
        self.assertEqual(audio_length, len(eaf.convert_csv_to_dico('../dataset/Fr_annotate.csv')))