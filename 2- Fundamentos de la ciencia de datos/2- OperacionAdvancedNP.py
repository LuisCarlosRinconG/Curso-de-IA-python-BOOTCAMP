# Tema= Difución en Numpy (broadcasting)

'''
Permite a numpy realizar operaciones aritmeticas en matrices de diferentes formas
las matrices mas pequeñas se espanden automaticamente para coincidir con la forma 
de las matrices mas grandes, algunas de las reglas de la difución incluyen que:
-las dimensiones se alinean desde la derecha
- una dimensión es compatible si:
    -coincide con la dimensión de la otra matrix:
    -una de las dimensiones es 1
'''

import numpy as np

# array and scalar broadcasting
arr=np.array([1,2,3])

#suma 10 a cada elemento
print(arr+10)

#matriz y vector
matrix = np.array([[1,2,3],[4,5,6]])
print('original\n',matrix)
vector = np.array([1,0,1])
print('modificada\n',matrix+vector)


#--------------------------------------------------\
#funciones de agregacion
'''
calcula estadisticas resumidas para arrays
'''

arr=np.array([[1,2,3],[4,5,6]])

print("SUMA: ",np.sum(arr))
print("MEDIA: ",np.mean(arr))
print("MAXIMO: ",np.max(arr))
print("MINIMO: ",np.min(arr))
print("DESVIACION ESTANDAR: ",np.std(arr))
print("SUMAR FILAS: ",np.sum(arr,axis=1))
print("SUMAR columnas: ",np.sum(arr,axis=0))



#--------------------------------------------------\
#Indexado booleano y filtrado

''''
El indexado booleano es cuando se usan matrices booleanas o condiciones para filtrar elementos
de una matriz
ejemplo:
'''

arr=np.arange(1,7)

#filtrar todos los números pares

avens=arr[arr%2==0]
print('pares:',avens)

#modificar los elementos basados en una condicion particular
arr[arr>3]=0
print('Modificar array: \n',arr)

#--------------------------------------------------\
#Generacion de numeros aleatorios y establecimiento de semillas

#Generacion de numeros aleatorios con numpy, numpy proporciona np.random

#generar decimales random
random_array=np.random.rand(3,3)
print(random_array)

#generar enteros en lugar de decimales
random_integers=np.random.randint(0,10,size=(2,3))
print(random_integers)

#Establecer semillas aleatorias
'''Se establece en este caso una semilla que es 42 y lo que hara es guardar
los numeros aleatorios dentro de si haciendo que nunca mas cambien '''
# muy util para ejecutar modelos de prueba

np.random.seed(42)

#Estos numeros se quedaran igual sin importar cuanto ejecute el programa
random_integers=np.random.randint(0,10,size=(2,3))
print(random_integers)





# Ejercicios propuestos

#broadcasting de matrix y vector
matriz=np.array([[1,2,3],[4,5,6],[7,8,9]])

vector=np.array([1,0,-1])

result=matriz + vector

print('broaedcasting vector \n',result)

#broadcasting de matrix y escalar

print('broaedcasting Escalar\n',result*45)

#Ejercicio: Generar y filtrar un conjunto de datos aleatorios

m_aleatoria=np.random.randint(0,100,size=(3,3))

print('matriz aleatoria:\n',m_aleatoria)

f_pares=m_aleatoria

print('matriz filtrando pares: \n',f_pares[f_pares%2==0])

f_inpares=m_aleatoria

f_inpares[f_inpares%2!=0]=0

print('matriz remplazando inpares por ceros \n', f_inpares)

#ahora calcular la desviación estandar

std=m_aleatoria.std()

std_2=np.std(m_aleatoria)

print(std)
print(std_2)