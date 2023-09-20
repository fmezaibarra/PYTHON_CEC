"""
Funcion que obtiene el numero de dias para un año y un mes dado


Importate recordar que por ser un ano bisiesto el mes de febrero tendra 29 Dias
y es por eso que la condicion isYearLeap dentro de la funcion daysInMonth es verdadera.

Autor: Fernando Meza Ibarra
"""



def isYearLeap(year):
    return(year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
 
def daysInMonth(year, month):
    diasPorMes = [31,28,31,30,31,30,31,31,30,31,30,31]    
    if isYearLeap(year):
        if diasPorMes[month - 1] == 28:
            return 29
        else:
            return diasPorMes[month - 1]
    else:
        return diasPorMes[month - 1]
    return None
 
# Entrada de datos (año, mes y días)    
testYears = [1999, 2000, 2016, 1987]
testMonths = [3, 2, 1, 11]
testResults = [28, 29, 31, 30]
diasPorMes=[]
total_dias_yr = 0
total_dias_mo = 0
nombreMes =["Enero", "Febrero", "Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
a_bisiestos =[]

for i in range(len(testYears)):
    yr = testYears[i]
    mo = testMonths[i]
    dd = testResults[i]
    a_bisiestos.append(isYearLeap(yr))
    print(yr,mo,dd, end=(" ==> "))
    
    if a_bisiestos[i]:  # Son años bisiestos        
        
        if daysInMonth(yr, mo) == dd:
            if  daysInMonth(yr, mo):
                print(yr,"Es bisiesto y", nombreMes[mo-1]," tiene ",daysInMonth(yr, mo)," días")
            else:
                print("fer")
        else:
            print(yr,"Es bisiesto y", nombreMes[mo-1]," tiene ",daysInMonth(yr, mo)," días y No ",dd)
    else:
        if dd != daysInMonth(yr, mo):
            print(yr,"No es bisiesto y",nombreMes[mo-1]," tiene ",daysInMonth(yr, mo)," días y No ",dd)            
        else:    
            print(yr,"No es bisiesto y",nombreMes[mo-1]," tiene ",daysInMonth(yr, mo)," días")
"""    
   
Años bisiestos desde 1976
1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020,
2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052, 2056, 2060, 2064, 2068, 
2072, 2076, 2080, 2084, 2088, 2092, 2096.

testYears = [1999, 2000, 2016, 1987]
testMonths = [3, 2, 1, 11]
testResults = [28, 29, 31, 30]
"""