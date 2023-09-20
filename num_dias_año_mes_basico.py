# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 12:28:53 2023

@author: fmezai
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
 
testYears = [1999, 2000, 2016, 1987]
testMonths = [3, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
 
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")
