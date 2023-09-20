# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 15:26:29 2023

@author: fmezai
"""

def fun(x,y):
    if x == y:
        return x
    else:
        return fun(x,y-1)

print(fun(0,3))