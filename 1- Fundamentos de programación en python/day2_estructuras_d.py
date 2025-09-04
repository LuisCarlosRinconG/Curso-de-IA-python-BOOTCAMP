#listas
lista = [1,2,'Algo',5,5.3]

lista.append("otro") 
lista.insert(1,'Cambio')

print(lista[:])

del lista[1]

print(lista)

lista.pop()

print("listas",lista)


# tuples

tupla=(1,5,6,"algo")

print("tuplas",tupla[1])
# Diccionarios

diccionario={"valor1":5,"valor2":3,"nombre":"luis"}

print(diccionario['valor1'])

diccionario["valor1"]="nuevo valor"

diccionario.pop("nombre")

for key,valor in diccionario.items():
    print("Del diccionario la clave es: ",key," y el valor es: ",valor)


# Conjuntos

set1={1,2,3}
set2={3,4,5}

set1.add(4)
set1.remove(4)

print('la union de los conjuntos es:', set1|set2)

print('la intersección de los conjuntos es:', set1&set2)

print('la diferencia del conjunto 1 en el conjunto 2 es:', set1-set2)
