# -*- coding: utf-8 -*-
"""Colab train

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UOBirvPC7gVl49qD_3nHk9r0DVFSgM16
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

from google.colab import drive
drive.mount('/content/drive')

"""Data"""

country_height = pd.read_csv("/content/drive/MyDrive/Data/NCD_RisC_Lancet_2020_height_child_adolescent_country (1).zip")
country_height.head()

gdp_constant = pd.read_csv("/content/drive/MyDrive/Data/P_Data_Extract_From_Global_Economic_Prospects.zip (Unzipped Files)/de433496-a47e-4409-a1ee-560980c3cdb3_Data.csv")
gdp_constant.head()

global_food = pd.read_csv("/content/drive/MyDrive/Data/global-food.csv")

global_food.head()

"""combine data"""

combined_data = pd.merge(country_height, gdp_constant, left_on="Country", right_on="Country Name")
combined_data.head()
len(combined_data)
#combined.iloc[10000]
#len(combined) #to see how many data sets
#life_expectancy= pd.read_csv("/content/drive/MyDrive/Data/Life expectancy.csv")
#life_expectancy.head()
#Fcombined_data=pd.merge(combined_data,life_expectancy, left_on="Entity". right_on ="Country Name")
#len(combined)



"""plot data"""

plt.scatter(x="2020 [2020]" ,y="Mean height",data=combined_data[combined_data["Sex"]=="Boys"])

plt.scatter(x="Year" ,y="Mean height",s=10,data=combined_data)
plt.xlabel("Year")
plt.ylabel("Mean height")
plt.title("Full Dataset")

plt.scatter(x="Age group" ,y="Mean height",data=combined_data[combined_data["Country Name"]=="America"])

"""Drop collums for test"""

plt.scatter(x="Age group" ,y="Mean height",data=combined_data[combined_data["Country Name"]=="India"])

from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeRegressor
df = pd.read_csv('/content/drive/MyDrive/Data/NCD_RisC_Lancet_2020_height_child_adolescent_country (1).zip')
y = combined_data['Mean height']
X = combined_data.drop(columns='Mean height',)

#Country Name, Country Code, Sex, Series Name, Series Code, Country
# Country Code, Series Name, Series Code, Country

df_dummy_sex= pd.get_dummies(df["Sex"])
print(df_dummy_sex)

df_dummy_country= pd.get_dummies(df["Country"])
print(df_dummy_country)

df_dummy_year= pd.get_dummies(df["Year"])
df_dummy_year=pd.DataFrame()


#trial_df= pd.get_dummies(df["Sex"])
#print(trial_df)

df.head()

test_dummy= pd.get_dummies(df["Sex"])
test_dummy

ctest_df=pd.concat([df.reset_index(drop=True), df_dummy_sex, df_dummy_country, df_dummy_year], axis=1)
ctest_df.head()

print(ctest_df.columns)

ctest_df.head()

#trial_df.drop('Sex', axis=1, inplace=True)
#atrial_df.head()

ctest_df.drop('Year', axis=1, inplace=True)
ctest_df.drop('Sex', axis=1, inplace=True)
ctest_df.drop('Mean height lower 95% uncertainty interval', axis=1, inplace=True)
ctest_df.drop('Mean height upper 95% uncertainty interval', axis=1, inplace=True)
ctest_df.drop('Mean height standard error', axis=1, inplace=True)
ctest_df.drop('Country', axis=1, inplace=True)
ctest_df.head()

print(ctest_df.columns)

y = ctest_df['Mean height']
X = ctest_df.drop(columns=['Age group','Mean height'],)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
#print(X_train)
#print(y_train)
#print(ctest_df)

ctest_df.head()

print(X)

"""Decision Tree Regressor"""

#print(list(X_train.dtypes))
#print(y_train.dtypes)
ctest_df["Age group"]

regression_model = DecisionTreeRegressor()
regression_model.fit(X_train, y_train)
#breaks down the dataset into smaller sets, until it gets to a closer subset where, it can predict a valid result.

from sklearn.metrics import mean_absolute_error

y_pred = regression_model.predict(X_test)
mean_absolute_error(y_test, y_pred)

from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

# Initialization
A_regression_model = DecisionTreeRegressor(max_depth=2, random_state=0)

#Training
A_regression_model.fit(X_train, y_train)

# Prediction
predictions = A_regression_model.predict(X_test)

# STEP 4: Evaluation
mean_absolute_error(y_test, predictions)

"""Linear regression"""

from sklearn.linear_model import LinearRegression

linear_model = LinearRegression()

linear_model.fit(X_train, y_train)



from sklearn.metrics import mean_absolute_error

y_pred = regression_model.predict(X_test)
mean_absolute_error(y_test, y_pred)

import matplotlib.pyplot as plt
plt.scatter(y_pred,y_test, s=1)
plt.xlabel("prediction")
plt.ylabel("True height")
plt.title("Model  prediction results ")
plt.show()

"""Random forest

"""

from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression
#X, y = make_regression(n_features=35, n_informative=2,random_state=0, shuffle=False)
regr = RandomForestRegressor(max_depth=2, random_state=0)
regr.fit(X_train, y_train)
RandomForestRegressor(...)

y_pred = regr.predict(X_test)
mean_absolute_error(y_test, y_pred)



"""# tests

TEST
"""

# = ctest_df.drop(columns=['Age group','Mean height'],)#linear regression, logistic regression, neural network, (random search)
#y = ctest_df['Mean height']
#from sklearn.neighbors import KNeighborsClassifier
#neigh = KNeighborsClassifier(n_neighbors=3)
#neigh.fit(X, y)

from sklearn.metrics import mean_squared_error
y_pred = regression_model.predict(X_test)
mean_squared_error(y_test, y_pred)

from sklearn.metrics import r2_score
y_pred = regression_model.predict(X_test)
r2_score(y_test, y_pred)

"""**linear** regression"""

#from sklearn.datasets import load_iris
#from sklearn.linear_model import LogisticRegression
#X, y = load_iris(return_X_y=True)
#a_linear_model= LogisticRegression()
#clf = LogisticRegression(random_state=0).fit(X, y)
#a_linear_model.fit(X_train, y_train)

"""Neural Network"""

#from sklearn.neural_network import MLPRegressor
#from sklearn.datasets import make_regression
#from sklearn.model_selection import train_test_split
#X, y = make_regression(n_samples=200, random_state=1)