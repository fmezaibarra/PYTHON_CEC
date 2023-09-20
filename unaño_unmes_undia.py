# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 09:39:25 2023

@author: Fernando Meza Ibarra
"""

def isYearLeap(year):   # True si es bisiesto, False si no.
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def daysInMonth(year, month):  # Devuelve número de días del mes (febrero 29 si es bisiesto, 28 si no)
    febDays = 29 if isYearLeap(year) else 28
    monthDays = [31, febDays, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return monthDays[month - 1]


def dayOfYear(year, month, day):  # Devuelve la suma de los dias transcurridos, dados el año, mes y día.
    sum = 0
    febDays = 29 if isYearLeap(year) else 28
    dias_por_mes = [31, febDays, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(month):
        sum += dias_por_mes[i]
    return sum    


# INICIO

nombreMes =["Enero", "Febrero", "Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]

bandera = 1
while bandera == 1:    
    ano = int(input("\nIngresar el año:"))
    mes = int(input("Ingresar el mes:"))   
    dia = int(input("Ingresar el dia:"))    
    print(f"\nHemos ingresado el año {ano}, el mes {nombreMes[mes-1]} y el día {dia}\n")    
    td = dayOfYear(ano, mes-1, dia) + dia
    print("Total días trascurridos: ", td)   
    sn = input(("\nContinuar (S/N): "))
    if sn == "s" or sn == "S":
        bandera = 1
    else:
        bandera = 0
        

print("\nAdiós!...Fin ejecución")    

# FIN