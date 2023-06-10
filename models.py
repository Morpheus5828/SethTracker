import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics

fr_feature = pd.read_csv("evaluation/Fr_features")
# fr_feature.head()

X = fr_feature[['rate', 'intensity']]
Y = fr_feature['grade']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)
regressor = RandomForestRegressor()
Y_predict = regressor.fit(X_train, Y_train).predict(X_test)

print(metrics.r2_score(Y_test, Y_predict))