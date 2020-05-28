# -*- coding: utf-8 -*-
"""
Created on Wed May 27 22:58:02 2020

@author: u23c37
"""

# matplotlib kütüphanesi
# görselleştirme kütüphanesi
# line plot, scatter plot, bar plot, subplots, histogram

import pandas as pd

df = pd.read_csv("iris.csv")

print(df.columns)
print(df.Species)
print(df.Species.unique())
print(df.info())
print(df.describe())

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

print(setosa.describe())
print(versicolor.describe())


import matplotlib.pyplot as plt

df1 = df.drop(["Id"],axis = 1)

#df1.plot()
#plt.show()

plt.plot(setosa.Id,setosa.PetalLengthCm, color = "red",
         label = "setosa")
plt.plot(versicolor.Id,versicolor.PetalLengthCm, color = "green",
         label = "versicolor")
plt.plot(virginica.Id,virginica.PetalLengthCm, color = "blue",
         label = "virginica")

plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.legend()
plt.show()

# %% Scatter plot

plt.scatter(setosa.PetalLengthCm, setosa.PetalWidthCm, color = "red"
            , label = "setosa")
plt.scatter(versicolor.PetalLengthCm, versicolor.PetalWidthCm, color = "green"
            , label = "versicolor")
plt.scatter(virginica.PetalLengthCm, virginica.PetalWidthCm, color = "blue"
            , label = "virginica")
plt.legend()
plt.xlabel("PetalLengthCm")
plt.ylabel("PetalWidthCm")
plt.title("Scatter Plot")
plt.show()

# %% Histogram plot

plt.hist(setosa.PetalLengthCm, bins = 20)
plt.xlabel("PetalLengthCm values")
plt.ylabel("frekans")
plt.title("Histogram")
plt.show()

# %% Bar plot

import numpy as np

x = np.array([1,2,3,4,5,6,7])
y = x * 2 + 5

plt.bar(x , y)
plt.title("bar plot")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# %% Subplot

#df1.plot(grid = True, alpha = 0.9, subplots = True)
plt.show()

plt.subplot(3,1,1)
plt.plot(setosa.Id,setosa.PetalLengthCm, color = "red",
         label = "setosa")
plt.ylabel("setosa - PetalLengthCm")
plt.subplot(3,1,2)
plt.plot(versicolor.Id,versicolor.PetalLengthCm, color = "green",
         label = "versicolor")
plt.ylabel("versicolor - PetalLengthCm")
