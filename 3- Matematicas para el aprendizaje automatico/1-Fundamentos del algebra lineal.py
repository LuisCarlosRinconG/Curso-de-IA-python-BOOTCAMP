'''
*vectores y matrices

Vector= Es un arreglo unidimensional que representa cantidades con magnitud y dirección
    Ejemplo: [2,3,4]

    -propiedades: Un venctor es un caso especial de una matriz con una fila o columna

Matrix= Es una area bidimensional de números organizados en filas y columnas

    Ejemplo: |2 -3  1 |
             |2  0 -1 |
             |1  4  5 |


    -propiedades: La matriz se leé como 3x3 o NxM donde M son las filas y N las columnas 
    
-----------------------------------------------------------------------------------------------

Operaciones con matrices:

- Adición y substracción: Las matrices deben  tener las mismas dimensiones para las operaciones 
elemento por elemento
PJ:
'''

import numpy as np

matriz1=np.array([[1,2],[3,4]])
matriz2=np.array([[5,6],[7,8]])

print("Suma:\n", matriz1+matriz2)
print("Resta:\n",matriz1-matriz2)

''''
-Multiplicación escalar: Esta no es un multiplicación de matrices, Es cuando se multiplica
cada elemento de la matriz pou un escalar
'''

matriz=np.array([[1,2],[3,4]])

M_escalar=matriz*4

print("La matriz multiplicada por escalar es:\n",M_escalar)

''''
-Multiplicación de matrices: Requiere que el numero de columnas 
en la primera matriz sea igual al numero de filas en la segunda matriz
'''

A=np.array([[1,2],[3,4]])
B=np.array([[5,6],[7,8]])

''''
        |1 2|
        |3 4|

        |5 6|
        |7 8|  

        Calculo de primera fila: 1*5 + 2*7 = 19 (Primera fila × primera columna)
        Calculo de Segunda fila: 1*6 + 2*8 = 22 (Primera fila × segunda columna)
        Calculo de Tercera fila: 3*5 + 4*7 = 43 (Segunda fila × primera columna)
        Calculo de Cuarta  fila: 3*6 + 4*8 = 50 (Segunda fila × segunda columna)

        |19 22|
        |43 50| 
'''

result=np.dot(A,B)

print("matriz multiplicada \n",result)

''''
-Matrices especiales: 
    Matriz identidad(I): Linea de unos diagonales rodeada por ceros

'''

I=np.eye(3)
print("matriz identidad: \n",I)


''''
-Matrices especiales: 
    Matriz cero(I): matriz con todos los elementos como cero
'''

z=np.zeros((3,3))
print("Matriz cero \n",z)

''''
-Matrices especiales: 
    Matriz diagonal(I): Es una matriz cuadrada donde todos los 
    elementos excepto los de la diagonal son cero
'''

D=np.diag([1,2,3])

print('matriz diagonal\n',D)

#Ejercicios practicos

#jercicio1: Crear vectores y matrices uzando numpy

M_uno=np.array([[1,2],[3,4]])
M_dos=np.array([[9,8],[7,6]])

# suma
sum=M_uno+M_dos
print('La suma es:\n',sum)

#resta
resta=M_uno-M_dos
print('La resta es:\n',resta)


# Multiplicación por escalar:
escalar=M_uno+5
print('La escalar es:\n',escalar)


# Multiplicacion:
Multiplicacion=np.dot(M_uno,M_dos)
print('La escalar es:\n',Multiplicacion)

# Multiplicacion de matriz por vector:

matriz=np.array([[5,6,8],[5,8,4],[2,1,3]])
vector=np.array([5,6,8])

Multiplicacionvector=np.dot(matriz,vector)
print('La multiplicacíón por vector es:\n',Multiplicacionvector)
