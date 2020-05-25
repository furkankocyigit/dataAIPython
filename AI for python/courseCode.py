# -*- coding: utf-8 -*-
"""
Created on Sun May 24 20:57:32 2020

@author: u23c37
"""

def hesapla(yas, kilo, *args):
    print(len(args))
    output = yas + kilo + args[0] + args[1]
    
    return output

hesapla(1,2,4,5)

# %%
#lambda function

def hesapla(x):
    output = x * x
    return output

sonuc = hesapla(3)

sonuc2 = lambda x: x * x
print(sonuc2(3))

# %% 
# List

liste = [1,2,3,4,5,6,7,8]
type(liste)

value = liste[1]

last_value = liste[-1]

ilk_üc_eleman = liste[0:3]
ikiden_sonra = liste[2:]

#%%
# Tuple

t = (1,3,3,4,5,6)

number_off_3_in_tupple = t.count(3)


# %%
# Dictionary

dictionary = {"ali"  : 32,
              "veli" : 45,
              "ayse" : 13
              }
# ali, veli ,ayse = keys
# 32,45,13 = values
dictionary.keys()
dictionary.values()

# %%

#hangi yüzyılda olduğunu dönen fonksiyon
#input = year >> 1<year<<2005

def year2Century(year):
    
    str_year = str(year)
    
    if(len(str_year)<3):
        return 1
    elif(len(str_year) == 3):
        if(str_year[1:3] == "00"):      #100 200 300
            return int(str_year[0])
        else:                           # 190 250 450
            return int(str_year[0]) + 1
    
    else:                               #1750 1700 1805
        if(str_year[1:3] == "00"):      #1700 ,1800, 1900
            return int(str_year[:2])    
        else:                           #1705 1645 1258
            return int(str_year[:2]) + 1#
        
        
            

