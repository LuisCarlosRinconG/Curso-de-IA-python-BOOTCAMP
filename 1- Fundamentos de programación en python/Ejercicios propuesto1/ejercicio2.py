#multiplicar todos los numeros de 1 a 100

from functools import reduce

lista =[]
for i in range (1,101):
    lista.append(i)
print(lista)

producto = reduce(lambda x,y: x*y,lista)
print(producto)