from unittest import TestCase

import numpy
import numpy as np

import extract_feature
import extract_feature as ef


class Test(TestCase):
    def test_get_rate(self):
        self.assertEqual(3, len(ef.get_rate("../dataset/Fr/F.24.mp3")))
        self.assertEqual(8, len(ef.get_rate("../dataset/Fr/F.202.mp3")))
        self.assertEqual(numpy.ndarray, type(ef.get_rate("../dataset/Fr/F.24.mp3")))

    def test_get_audio_time(self):
        self.assertEqual(1.27, ef.get_audio_time("../dataset/Fr/F.24.mp3"))
        self.assertEqual(13.43, ef.get_audio_time("../dataset/Fr/H.24.mp3"))
        self.assertEqual(float, type(ef.get_audio_time("../dataset/Fr/F.24.mp3")))

    def test_get_intensity(self):
        self.assertEqual(numpy.ndarray, type(ef.get_intensity("../dataset/Fr/H.24.mp3")))
        self.assertEqual(257, len(ef.get_intensity("../dataset/Fr/H.24.mp3")))

    def test_extract_rate_vector(self):
        self.assertEqual(numpy.ndarray, type(ef.extract_rate_vector("../evaluation/Fr_features")))
        self.assertEqual(575, len(ef.extract_rate_vector("../evaluation/Fr_features")))

    def test_extract_intensity_vector(self):
        self.assertEqual(numpy.ndarray, type(ef.extract_intensity_vector("../evaluation/Fr_features")))
        self.assertEqual(575, len(ef.extract_intensity_vector("../evaluation/Fr_features")))

    def test_extract_grade_vector(self):
        self.assertEqual(numpy.ndarray, type(ef.extract_grade_vector("../evaluation/Fr_features")))
        self.assertEqual(575, len(ef.extract_grade_vector("../evaluation/Fr_features")))

'''    def test_extract_sample_rate(self):
        self.assertEqual(numpy.ndarray, type(ef.extract_sample_rate("../evaluation/Fr_features", ["F.1.mp3"])))
        self.assertEqual(1, len(ef.extract_sample_rate("../evaluation/Fr_features")))

    def test_extract_sample_intensity(self):
        self.fail()

    def test_extract_sample_grade(self):
        self.fail()'''
