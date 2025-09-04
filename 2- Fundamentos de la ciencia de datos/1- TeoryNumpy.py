import numpy as np

# crear matrices
''''hay diferentes maneras como:'''
#a partir de una lista
arr = np.array([1,2,3,4])

print(arr)

# uso de funciones integradas

# crear matriz de 3x3 de ceros
matrizcero= np.zeros((3,3))
print(matrizcero)

# crear matriz de 2x4 de cunos
matrizunos= np.ones((2,4))
print(matrizunos)

# Devolver valores x disdantes dentro de un intervalo dado
#pj: obtener numeros del 1 al 10 pero con un intervalo de 2
range_array = np.arange(1,10,2)
print(range_array)

#Devolver numeros espaciados uniformemente sobre un intervalo especifico especificado
# En pocas palabras distribuye un rango en partes iguales
linspace_array=np.linspace(0,10,3)
print(linspace_array)



#-----------------------------------------------------------------------
# Manipulación de matrices

# convertir a matriz
arr=np.array([1,2,3,4,5,6])
remodelar=arr.reshape((2,3))
print(remodelar)

# añadir dimensiones
arr =np.array([1,2,3])
espandir=arr[:,np.newaxis]
print(espandir)

#-----------------------------------------------------------------------------------------------------
# Operaciones basicas en arreglos

a=np.array([1,2,3])
b=np.array([4,5,6])

# sumar arreglos
print(a+b)
#multiplicacion
print(a*b)
#division
print(a/b)

# operaciones matematicas
arr=np.array([4,16,25])
print(np.sqrt(arr))
print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))

#--------------------------------------------------------------------------
# indexado, corte y restruccturación de arrays

#indexado

arr=np.array([10,20,30,40,50,60])

print(arr[2])

#corte

print(arr[1:4])

#restruccturación

restructurar=arr.reshape(2,3)
print(restructurar)



#Ejercicio: crear una matriz de 5*5 y sumar todos sus numeros

import numpy as np

#matriz=np.array([[],[],[]])

#Ejemplo: matriz de 4x4 con números enteros entre 1 y 100
#matriz = np.random.randint(1, 101, size=(4, 4))


arreglo=np.arange(25)

arrmatriz=arreglo.reshape((5,5))
print(arrmatriz)

print(np.sum(arrmatriz))