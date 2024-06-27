from week4 import*
import pytest
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import numpy as np

def test5():
	assert( round(getStatistic()['X5 latitude'][5],2 )== round(24.9711,2) )
	assert( round(getStatistic()['X2 house age'][0],2) == round(414.0,2) )
	assert( round(getStatistic()['X6 longitude'][1],2) == round(121.53336108695667,2) )


def test6():
	
	X_train1, X_test1, y_train1, y_test1 = split()
	df_X_train = pd.read_csv("testcase/xtrain.csv", index_col=0)
	df_X_test = pd.read_csv("testcase/xtest.csv", index_col=0)
	df_y_train = pd.read_csv("testcase/ytrain.csv", index_col=0)
	df_y_test = pd.read_csv("testcase/ytest.csv", index_col=0)

	# assert(all(df_X_train == X_train1))
	assert(all(df_X_test == X_test1))
	assert(all(df_y_train == y_train1))
	assert(all(df_y_test == y_test1))

def test7():

	coefficients1, intercept1, mse1, rmse1, r2_score1 = makeModel()

	assert np.allclose(coefficients1[0], np.array([-2.70593236e-01,-4.55249601e-03,1.10512079e+00, 2.36092831e+02,
  -2.39036942e+01]))
	assert np.allclose(intercept1, np.array([-2946.65885903]))
	assert np.allclose(mse1, np.float64(54.580945200862395))
	assert np.allclose(rmse1, np.float64(7.387891796775477))
	assert np.allclose(r2_score1, np.float64(0.674648138282816 ))
