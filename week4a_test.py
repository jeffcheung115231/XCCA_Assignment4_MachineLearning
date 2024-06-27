from week4 import*
import pytest
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import math
import pandas as pd
import numpy as np

df = pd.read_csv("data/realestate.csv")

def test1():
	assert all(load().head() == df.head())


def test2():
	df.drop(['No'],axis='columns', inplace=True)
	df.drop(['X1 transaction date'], axis='columns' ,inplace=True)
	assert getShape() == (414, 6)

def test3():
	assert getInfo() == df.info()


def test4():
	dict = {"X2 house age":0, "X3 distance to the nearest MRT station": 0,"X4 number of convenience stores":0,"X5 latitude":0, "X6 longitude":0, "Y house price of unit area":0}
	assert all(checkNull() == pd.Series(dict))
