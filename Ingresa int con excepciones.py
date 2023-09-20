# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 15:57:11 2023

@author: fmezai
"""


def readint(prompt, min, max):
    try:
        x=int(input("Entre un número de -10 a 10: "))
        assert x>=min and x<=max 
        #print("El número es: ",x) 
    except ValueError:
            print("Error: Ingreso incorrecto") 
            x = 0
    except AssertionError: 
        print("Error: el valor no está en el rango permitido (",min," a ",max,")")
    return x
    

v = readint("Entre un múmero entre  -10 a 10: ", -10, 10)

print("El número es:", v)