# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os    # Se requiere para limpiar la pantalla de la terminal de salida

	
borrarPantalla = lambda: os.system ("cls")
borrarPantalla() # Limpia la pantalla

print("EJEMPLO DEL USO DE INPUT\n ")

nombre = nombre = input("Ingrese su Nombre: ")
apellido = input("Ingrese su Apellido: ")
ubicacion = input("Ingrese su bicación: ")
edad = input("Ingrese su Edad: ")

print("Usted es: ",nombre,apellido," se localiza en:", ubicacion,"y su edad es", edad, "años")

