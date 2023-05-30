import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.ensemble import GradientBoostingRegressor
import extract_feature as ef

# Regression polynomial

feature_path = "./evaluation/Fr_features"

rate = ef.extract_rate_vector(feature_path)
grade = ef.extract_grade_vector(feature_path)
#freq = ef.extract_rate_vector(feature_path)
intensity = ef.extract_intensity_vector(feature_path)




#X_train, X_test, Y_train, Y_test = train_test_split(x, rate, test_size=0.2)

        



