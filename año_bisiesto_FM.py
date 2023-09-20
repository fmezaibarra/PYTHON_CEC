# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 11:25:18 2023

@author: fmezai
"""

# En el calendario gregoriano, un año normal consta de 365 días. 
# Debido a que la duración real de un año sideral (el tiempo necesario para que la Tierra gire una vez alrededor del Sol)
# es en realidad 365.2425 días, un "año bisiesto" de 366 días se utiliza una vez cada cuatro años para eliminar el error
# causado por tres años normales (pero cortos). 
# Cualquier año divisible por 4 es un año bisiesto: por ejemplo, 1988, 1992 y 1996 son años bisiestos.

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
    
testData = [1900, 2000, 2016, 1988,2023]
testResults = [False, True, True, False, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")

"""
Conclusión de la ejecución:
La lista de años y la lista de resultados se recortren uno a uno.
Segun ello: 
Para que todo salga OK, los años de la primera, cuarta y quinta posición NO deben ser años bisiestos.
Pero en el caso de testData, el año 1988 es bisiesto, pero en la lista testResults dice que es FALSe, por ello sale FAILED    

SALIDA
1900 ->OK
2000 ->OK
2016 ->OK
1988 ->Failed
2023 ->OK

"""
