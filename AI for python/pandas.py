# -*- coding: utf-8 -*-
"""
Created on Tue May 26 22:58:42 2020

@author: u23c37
"""

# 1- pandas hızlı ve etkili for dataframes
# 2- csv ve text dosyalarını açıp inceleyip sonuçlarımızı da rahatca kaydedebiliriz ve kendi aralarında geçişler kolaydır
# 3- pandas bizim işimizi kolaylaştırıyor for missing data
# 4- reshape yapıp datayı daha etkili bir şekilde kullanabiliriz
# 5- slicing ve indexing kolay yapılır
# 6- time series data analizinde çok yardımcı olur
# 7- ayrıca hız açısından optimize edilmiş hızlı bir kütüphanedir


import pandas as pd

dictionary = {"NAME": ["ali","veli","kenan","hilal","ayse","evren"],
              "AGE": [15,16,17,33,45,66],
              "MAAS": [100,150,240,350,110,220]}


dataFrame1 = pd.DataFrame(dictionary)

head = dataFrame1.head()
tail = dataFrame1.tail()

# %%
# pandas basic method


print(dataFrame1.columns)

print(dataFrame1.info())

print(dataFrame1.dtypes)

print(dataFrame1.describe())  # numeric feature = columns (age, maas)


# %% indexing and slicing

print(dataFrame1["NAME"])
print(dataFrame1["AGE"])
print(dataFrame1.NAME)
print(dataFrame1.AGE)

dataFrame1["yeni feature"] = [-1,-2,-3,-4,-5,-6]

print(dataFrame1.loc[:,"AGE"])
print(dataFrame1.loc[:3,"AGE"])
print(dataFrame1.loc[:3,"NAME":"MAAS"])

print(dataFrame1.loc[:3,["NAME","MAAS"]])
print(dataFrame1.loc[::-1])
print(dataFrame1.loc[:,:"MAAS"])

print(dataFrame1.iloc[:,2])