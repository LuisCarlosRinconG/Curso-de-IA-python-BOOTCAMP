''''''

# Determinantes e inversas de una matriz
'''
Un Determinante es un valor escalar que proporciona información sobre las propiedades de una matriz
como su invertibilidad.
    - Se calcula solamente para matrices cuadradas 
    - Algunas de las ideas claves sobre el determinante incluyen que si el determinante de una matriz A
    es igual a cero, la matriz A es singular, lo que significa que no es invertible
    mientras que si el determinante de A no es igual a cero, entonces es invertible
    -Representación geometrica
        -Para una matriz dos por dos, el determinante representa el factor de escala del are formada
        por sus vectores columna;Entonces, la formula se puede representar para una matriz dos por dos
        como el determinante de la matriz


        det         |A B|   =  AD-BC
                    |C D|  
'''

import numpy as np

A=np.array([[2,3],[1,4]])
''''
        det         |2 3|   =  (2*4)-(3*1) = 5
                    |1 4| 

'''
determinante=np.linalg.det(A)

print("El determinante es:\n",determinante)


# Inversa de una matriz 
'''
- Se denota como A elevado -1
- El producto de una matriz y su inversa es la matriz identidad
- Una matriz es invertible solo si el determinante de A no es cero
'''
B=np.array([[2,3],[1,4]])
inverse=np.linalg.inv(B)
print("inversa de una matriz\n",inverse)



#-----------------------------------------Valores propios y vectores propios------------------------
'''
Son propiedades de matrices cuadradas que describen transformaciones 

-Representación geometrica:
- Se puede hablar de vectores propios como un vector propio que apunta en la dirección donde la transformacióñ
de la matriz estira o comprime vectores
- Los valores propios indican la dirección de la transformación (Factor de estiramiento o compresión)

-Propiedades:
- Una matriz de tamaño n * n tiene n valores propios
- Los valores propios pueden ser reales o complejos
- Para una matriz simetrica los valores propios son siempre reales
'''

C=np.array([[2,3],[1,4]])
valorespropios,vectorespropios=np.linalg.eig(C)

print('los valores propios de la matriz son: \n',valorespropios,"\n y los vectores propios son: \n",vectorespropios)


# introducción a la descomposición de matrices
'''
Es un proceso de descomponer una matriz en componentes mas pequños para analizar o resolver problemas
,para este proceso se tiene:
    -Descomposición en valores singulares(SVD): Descompone una matriz A en tres matrices
    - Aplicaciones de SVD:
        -Reducción de dimensionalidad: Por ejemplo en el algoritmo de analisis de componentes
        principales (PCA) se utiliza 
        - Para la reducción de ruido en conjuntos de datos y aveces para la compresión de imagenes
'''

D=np.array([[2,3],[1,4]])

U,S,Vt=np.linalg.svd(A)
# U es el vector singular isquierdo
# S es la matriz diagonal de valores singulares que es no negativa
# Vt son los vectores singulares derechos tambien llamados V transpuesta
print('U:\n',U,'\n S:\n',S,'\n Vt\n',Vt) 