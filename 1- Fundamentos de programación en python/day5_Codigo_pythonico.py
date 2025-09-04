# Codigo pythonico:Buenas practicas

# Comprensiones de listas: para consolidar multiples lineas en una sola linea

#[expresion for item in iterable if condicion]

#Ejemplo:

#crear una lista de cuadrados
squares =[x**2 for x in range(10)]
print(squares)

# filtrar numeros pares de 10 a 20
events=[x for x in range(10,20) if x%2==0]
print(events)

# Funciones lambda(funciones en linea): Son funciones anonimas de una sola expresión definida usando la pal;abra clave lambda

# ejemplo

#lambda argumentos: expresion

add= lambda x,y: x+y
print(add(3,5))



# Funciones mas utilizadas en el curso

#Map(): Aplica una función a cada elemento en un iterable

#Ejemplo:

numbers=[1,8,7,5]
squares =map(lambda x: x**2, numbers)
print(list(squares))


#filter(): reduce o filtra elementos basandose en una condición

#Ejemplo:

numbers=[9,5,4,2]
evenlist=filter(lambda x:x%2 == 0,numbers)
print(list(evenlist))

#reduce(): reduce un iterable a un solo valor(numero)

#Ejemplo:

from functools import reduce

numbers=[4,9,2,2]
product = reduce(lambda x,y:x*y,numbers)
print(list(product))




# MODULOS(librerias) OS y SYS

# libreria os: proporciona funciones para interactuar con el sistema operativo en si,
# funciones como como crear un nuevo directorio, el;iminar archivos, etc.

import os 

print(os.getcwd()) # directorio actual
os.mkdir("test_dir") # crea un direcctorio
os.remove("file.txt") # eliminar archivos

#libreria SYS: Proporciona acceso a parametros y funciones especificas del sistema

import sys

print(sys.argv)#argumentos de linea de comandos
print(sys.version) # imprimir version de python