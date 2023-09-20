# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 12:02:31 2023

@author: fmezai


Verifica si la siguiente lista es año bisiesto 
1988, 1992 y 1996

"""

def isYearLeap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    

# 1900, 2000, 2016, 1987,2023
print(isYearLeap(1900))   