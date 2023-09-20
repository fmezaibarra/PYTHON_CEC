# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 15:10:45 2023

@author: fmezai
"""

IVA = 0.12

precioProducto = 100

precioIVA = precioProducto * IVA

print("El precio del IVA es", precioIVA, "$")

print("El precio final es", (precioIVA+precioProducto ) ,"$")