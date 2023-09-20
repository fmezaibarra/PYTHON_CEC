#!/usr/bin/env python
# coding: utf-8

# ![Título](Images/cisco.png)

# # Práctica de laboratorio: Realice el desafío de Python 
# 
# 
# Este es un ejercicio opcional para probar su conocimiento de los principios básicos de Python. Sin embargo, recomendamos fervientemente que el estudiante complete estos ejercicios para prepararse para el resto de este curso. Si no sabe cómo resolverlos, fíjese en las lecciones de Python disponibles en la carpeta de Materiales del curso/tutoriales y demostraciones.

# #### Responda las preguntas o complete las tareas detalladas a continuación; utilice el método específico descrito, si corresponde.

# #### 1) ¿Cuánto es 3 a la potencia de 5?

# In[1]:


# 3 elevado a la potencia 5

3**5


# #### 2) Cree una variable, *'s'*, que contenga la cadena "¡Este curso es increíble!". Con la variable, divida la cadena en una lista.

# In[4]:


# Crea cadena y la divide en una lista
s = "¡Este curso es increíble!"
lista = s.split()
print(s," ==>  ",lista)


# #### 3) Dadas las variables altura y montaña, use .format() para imprimir la cadena siguiente:
# <center>‘La altura del Monte Everest es de 8848 metros’.</center>

# In[5]:


# Impresión con formato

mountain = "Mt. Everest"
height = 8848
#print("...".format( ? , ? ))

print("La altura del {m} es {a} metros.".format( m=mountain, a=height ))


# #### 4) Dada la lista anidada siguiente, use la indexación para tomar la palabra '"esto"'.

# In[17]:


# Code cell 4
lst = ['a','b',[4,10,11],['c',[1,66,['this']],2,111],'e',7]
#lst[?][?][?][?]
print("Lista inicial: ", lst)
palabra = lst[3][1][2][0]
print("Palabra encontrada OK:",palabra)


# #### 5) Dado el diccionario anidado siguiente, tome la palabra "eso". Este ejercicio es un poco más difícil.

# In[25]:


# Buscat "that"

d = {'k1':['val1','val2','val3',{'we':['need','to','go',{'deeper':[1,2,3,'that']}]}]}

print("Diccionario incial: ",d)

print("palabra encontrada OK :", d["k1"][3]["we"][3]["deeper"][3])


# #### 6) ¿Cuál es la diferencia principal entre una tupla y una lista? 

# *Las Tuplas son inmutables, en tanto que las Listas son mutables. Significa que una vez creada una tupla, sus elementos no pueden cambiar. Las tuplas no pueden ser modificadas.*

# #### 7) Cree una función, GetDomain(), que tome el dominio del sitio web de correo electrónico de una cadena en la forma: 'user@domain.com'.
# Por ejemplo, el paso de "user@domain.com" daría: domain.com

# In[33]:


# Obtener el sufijo de una cuenta de correo electrónico.
def GetDomain(correo): 
    return correo.split("@")[-1]

print(GetDomain('fernando@aol.com'))


# #### 8) Cree una función básica, findInternet(), que dé una devolución de True si la palabra 'Internet' se incluye en la cadena de entrada. No se preocupe por los casos de perímetro como la puntuación que se asocia con la palabra, pero tenga en cuenta el uso de mayúsculas. (Sugerencia: vea https://docs.python.org/2/reference/expressions.html#in)

# In[40]:


# True si encuentra la palabra Internet en la cadena del parámetro

def findInternet(s):
    return 'internet' in s.lower().split()

cadena = 'The Internet wil Engineering Task Force was created in 1986'    
findInternet(cadena)


# #### 9) Cree una función, countIoT(), que cuente la cantidad de veces que la palabra "IdT" aparece en una cadena.  Ignore los casos de perímetro pero tenga en cuenta el uso de mayúsculas.

# In[44]:


# Cree una función, countIoT(), que cuente la cantidad de veces que la palabra "IdT" aparece en una cadena. 
# Ignore los casos de perímetro pero tenga en cuenta el uso de mayúsculas.


def countIoT(st):
    count = st.count("IoT")
    return count

st = countIoT('I don\'t know how to spell IoT ! Is it IoT or iot ? What does iot mean anyway?')
print(st," veces la palabra IoT")


# #### 10) Utilice las expresiones lambda y la función filter() para filtrar las palabras de una lista que no comiencen con la letra 'd'. Por ejemplo:
# 
#     sec = [“datos”, “sal”, “diario”, “gato”, “perro”]
# 
# debe ser filtrado a:
# 
#     ['datos', 'diario']

# In[57]:


# Filtrar o quitar las palabras de una lista que NO comiencen con la letra 'd'

seq = ['data','salt' ,'dairy','cat', 'dog']

print("Lista filtrada: ", list(filter(lambda x: x[0] =="d", seq)))
print("Elementos filtrados: ", list(filter(lambda x: x[0] !="d", seq)))


# #### 11) Utilice las expresiones lambda y la función map() para convertir una lista de palabras a mayúsculas. Por ejemplo:

# sec = [“datos”, “sal”, “diario”, “gato”, “perro”]
# 
# debe ser:
# 
#    [“DATOS”, “SAL”, “DIARIO”, “GATO”, “PERRO”]

# In[65]:


# Convierte una lista de elemento de minúsculas a mayúsculas.
# Usar list(map())

seq = ['data','salt' ,'dairy','cat', 'dog']
lista_mayuscula = list(map(lambda x: x.upper(), seq))

print(lista_mayuscula)


# #### 12) Imagine un termostato inteligente conectado a la puerta que pueda detectar, además de la temperatura, el momento en el que las personas entran o salen de la casa. 
# Escriba una función que, cuando la temperatura sea inferior a 20 ºC y haya personas en la casa (codificado como valor booleano que se envía como parámetro a la función), inicie la calefacción mediante la devolución de la cadena "calefacción encendida". Cuando la temperatura llegue a 23 grados o no haya personas en la casa, la función devuelve la cadena "calefacción apagada". Cuando no se cumpla ninguna de estas condiciones, la función es "No hacer nada".

# In[67]:


# Control de Calefacción de Termostato según entran y salen personas.
def termostato(temperatura, personas):
    if temperatura < 20 and personas == 1:
        print("Calefacción Encendida")
    elif temperatura == 23 or personas == 0:
        print("Calefacción Apagada")
    else:
        print("No hacer nada")
# Return command


# In[75]:


# Verificación con datos 
termostato(10,True)  # Cuando esta a 10 grados y existe una persona
termostato(25,False) # Cuando esta a 25 grados y no hay nadie
termostato(24,2)     # Cuando esta a 23 grados y no hay nadie 


# #### 13) La función zip(list1, list2) devuelve una lista de tuplas, donde la tupla i-th contiene el elemento i-th de cada una de las listas de argumento. Utilice la función zip para crear la siguiente lista de tuplas:

# 'comprimido = [(“Estacionamiento”, -1), (“Negocios”, 0), (“Área de restaurantes”, 1), (“oficinas”, 2)]'

# In[80]:


# Acondiciona a una nueva lista de tuplas 2 tuplas previas.
# Una tupa es de string (areas departamentales) y otra de enteros (número de piso)

floor_types = ['Estacionamiento', 'Negocios', 'Áreas de restaurantes', 'Oficinas']
floor_numbers = range(-1,3)

# Cuando usamos la función zip(), estamos uniendo uno o más iterables y cada unión de elementos resulta en una nueva tupla.
zipped = list(zip(floor_types, floor_numbers))  

print(zipped)  


# #### 14) Utilice la función zip y dict() para crear un diccionario, elevator_dict, donde las teclas sean los tipos de piso y los valores sean el número correspondiente del piso, de modo que:
# elevator_dict[- 1] = “Estacionamiento”

# In[92]:


# Uso de ZIP y DIC - Crea diccionario
floor_types = ['Estacionamiento', 'Negocios', 'Áreas de restaurantes', 'Oficinas']
floors_numbers = range(-1,3)

elevator_dict = dict(zip(floors_numbers, floor_types))

print(elevator_dict)


# In[94]:


# Verifica los elementos del nuevo Diccionario creado.

print(elevator_dict[-1]) # Elemento de la clave -1
print(elevator_dict[2])  # Elemento de la clave 2


# #### 15) Cree una clase de 'Ascensor'. El constructor acepta la lista de cadenas 'floor_types' y la lista de números enteros 'floor_numbers'. La clase implementa los métodos 'ask_which_floor' y 'go_to_floor'. La salida de estos métodos debe verse de la siguiente manera:
# `floor_types = ['Estacionamiento', 'Negocios', 'Área de restaurantes', 'Oficinas']
# floors_numbers = rango(-1,4)
# 
# el = Elevador(floor_numbers, floor_types)
# 
# el.go_to_floor(1)`
# 
# `¡Vaya al piso del área de restaurantes!`
# 
# `el.go_to_floor(-2)`
# 
# `En este edificio está el piso número -2.`
# 
# `El.ask_which_floor('Oficinas')`
# 
# `El piso de oficinas es el número: 2`
# 
# `El.ask_which_floor('Piscina')`
# 
# `No hay ningún piso con piscina en este edificio.`

# In[185]:


# Code cell 17
floor_types = ['Estacionamiento', 'Negocios', 'Área de restaurantes', 'Oficinas']
floor_numbers = range(-1,4)

class Elevator:
    
    def __init__(self, floor_numbers, floor_types):
        self._floor_numbers = floor_numbers
        self._floor_types = floor_types
        self._number_to_type_dict = dict(zip(floor_numbers, floor_types)) 
        self._type_to_number_dict = dict(zip(floor_types, floor_numbers)) 
        
    def ask_which_floor(self, floor_type):    
        if floor_type in self._floor_types:            
            print('El piso de {} es el número: {}.'.format(floor_type, self._type_to_number_dict[floor_type]))
        else:
            print('No hay ningún piso con {} en este edificio.'.format(floor_type))
    
    def go_to_floor(self, floor_number):
        if floor_number in self._floor_numbers:
            print('¡Vaya al piso {} de {}!.'.format(floor_number, self._number_to_type_dict[floor_number]))
        else:            
            print('En este edificio está el piso número  ({}).'.format(floor_number))    
            
    


# In[187]:


# Verifica qué Area esta en el piso 1
el = Elevator(floor_numbers, floor_types)

el.go_to_floor(1)


# In[188]:


# Verifica qué existe un piso (-2) en el edificio
el.go_to_floor(-2)


# In[189]:


# Verifica en que piso esta un área determinada (Oficinas)
el.ask_which_floor('Oficinas')


# In[190]:


# Verifica si en el edificio existe un area determinada (Deportes - Natación)
el.ask_which_floor('Piscina')


# # ¡Excelente trabajo!

# <font size='0.5'>© 2017 Cisco y/o sus filiales. Todos los derechos reservados. Este documento es información pública de Cisco.<font>
