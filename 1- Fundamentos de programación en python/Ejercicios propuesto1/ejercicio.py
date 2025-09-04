'''
Leer el archivo usando with.

Usar expresiones regulares para extraer solo los correos electrónicos válidos.

Usar una función lambda para convertir los correos válidos a minúsculas.

Mostrar en pantalla la lista de correos válidos ordenados alfabéticamente.
'''

#Leer el archivo usando with.
import re

try:
    with open('./Semana 1/Ejercicios propuesto1/usuarios.txt','r') as file:
        content=file.read()
        #print(content)
        #Usar expresiones regulares para extraer solo los correos electrónicos válidos.
        filtro=re.findall('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',content)
        print(filtro)

        # Convertir a minúsculas usando lambda
        correos_minuscula = list(map(lambda correo: correo.lower(), filtro))
        
        # Ordenar alfabéticamente
        correos_ordenados = sorted(correos_minuscula)

        print(correos_ordenados)

except FileNotFoundError:
    print('Archivo no encontrado')