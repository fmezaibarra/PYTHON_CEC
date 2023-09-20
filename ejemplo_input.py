# -*- coding: utf-8 -*-

# Spyder Editor

# Autor: Fernando Meza Ibarra

import os    # Se requiere para limpiar la pantalla de la terminal de salida

	
borrarPantalla = lambda: os.system ("cls")
borrarPantalla() # Limpia la pantalla

print("EJEMPLO DEL USO DE LA INSTRUCCIÓN INPUT\n ")

nombre = nombre = input("Ingrese su Nombre: ")
apellido = input("Ingrese su Apellido: ")
ubicacion = input("Ingrese su Ubicación: ")
edad = input("Ingrese su Edad: ")

print("Bienevenido a la Plataforma de Colaboración de Desarrollo GITHUB...\n")
print("Usted ha sido registrado como : ",nombre,apellido,", su ubicación es:", ubicacion," y su edad es", edad, "años")

