from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import math
import pandas as pd

Q1:
def load():
    df = pd.read_csv("/content/Real estate.csv")
    return df

df = load()
df.drop(['No'], axis='columns', inplace=True)
df.drop(['X1 transaction date'], axis='columns', inplace=True)

Q2:
def getShape():
    return df.shape
Q3:
def getInfo():
    return df.info()
Q4:
def checkNull():
    return df.isnull().sum()
Q5:
def getStatistic():
    return df.describe()
Q6:
def split():
    df_y = df[['Y house price of unit area']]
    df_X = df.drop(['Y house price of unit area'], axis='columns')
    X_train, X_test, y_train, y_test = train_test_split(df_X, df_y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test
Q9:
def makeModel():
    X_train, X_test, y_train, y_test = split()
    model = linear_model.LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    coefficients = model.coef_
    intercept = model.intercept_
    mse = mean_squared_error(y_test, y_pred)
    rmse = math.sqrt(mse)
    r2score = r2_score(y_test, y_pred)
    return coefficients, intercept, mse, rmse, r2score
