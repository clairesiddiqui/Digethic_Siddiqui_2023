import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle


# READ .CSV FILE
data = pd.read_csv('data/auto-mpg.csv', sep = ";")
print("Dataset:", data)


# SHUFFLE DATA
data = data.sample(frac=1)


# DECLARE TEST-AND TRAINING VARIABLES
y_variable = data['mpg']
x_variables = data.loc[:, data.columns != 'mpg']

x_train, x_test, y_train, y_test = train_test_split(x_variables, y_variable, test_size=0.2)


# APPLY LINEAR REGRESSION MODEL
regressor = LinearRegression()
regressor = regressor.fit(x_train, y_train)
y_pred = regressor.predict(x_test)


# SAVE OUTPUT USING PICKLE
file_to_write = open("data/models/baummethoden_lr.pickle", "wb")
pickle.dump(regressor, file_to_write)

