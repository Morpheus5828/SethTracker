import struct

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import extract_feature as ef
import tools as tl

feature_path = "./evaluation/Fr_features"

rate = ef.extract_rate_vector(feature_path)
grade = ef.extract_grade_vector(feature_path)
intensity = ef.extract_intensity_vector(feature_path)

fr_feature = pd.read_csv("evaluation/Fr_features")
#print(fr_feature.info)
print(sns.pairplot(fr_feature))



