[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/5Se3TjlK)
# FTDS-week4-test
 
###Week4 Test
This is a simple real estate price prediction problem\
Source URL: [https://www.kaggle.com/quantbruce/real-estate-price-prediction]\
#### Data Set Characteristic
Target: Column 11 is a quantitative measure of house price of unit area\
Attribute Information:\
 1   No                                      
 2   X1 transaction date                  
 3   X2 house age                            
 4   X3 distance to the nearest MRT station
 5   X4 number of convenience stores   
 6   X5 latitude          
 7   X6 longitude

 Please check that the csv file is in the data folder
 Just right click and select copy relative path
 ```bash
pd.read_csv('relative path of the file')
 ```

 follow the instructions in the week4.py file and only write your code within SOLUTION START and SOLUTION END
      
 feel free to plot any graph for data visualization but it will not be graded

### libraries needed
#### they are all imported for you 
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import math
import pandas as pd


