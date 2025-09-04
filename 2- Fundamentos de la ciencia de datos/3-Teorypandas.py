# '''

# '''
# #-------------------------------------------------------

# import pandas as pd

# # Este comando creara un diccionario donde cada dato esta indexado en un punto particular 
# #(Una lista convertida en un diccionario)
# s=pd.Series([10,20,30], index=["a","b","c"])
# print(s)

# #Creación de un dataframe
# data={"name":["Alice","Bob"],"Age":[25,30]}

# df=pd.DataFrame(data)
# print(df)


# #-------------------------------------------------------
# #Como cargar datos desde csv,excel, diccionarios o otras fuentes

# df=pd.read_csv("RUTA DEL ARCHIVO.csv")

# df=pd.read_excel("RUTA DEL ARCHIVO.xlsx")


# #-------------------------------------------------------
# #Guardado de datos en csv y excel

# nuevodf=pd.read_csv("RUTA DEL ARCHIVO.csv")

# #guardar
# nuevodf.to_excel("Ruta.xlsx")
# nuevodf.to_csv("Ruta.csv")

# # Para guardar la info sin indice se añade al final ,index=False

# nuevodf.to_excel("Ruta.xlsx",index=False)

# #-------------------------------------------------------
# #Operaciones basicas con DataFrame

# #Visualización de datos

# #Imprimir las primeras 5 filas de un conjunto de datos en particular
# print(df.head())

# # ver las ultimas filas
# print(df.tail())

# #Nota; Dentro de los parentesis se pueden especificar el número de filas a ver

# # Ver información completa del encabezado
# print(df.info())

# # Ver información estadistica detallada completa del encabezado
# print(df.describe())


# # ------------Selección e indexación---------

# #Imprimir una columna

# print(df["Nombre de la columna"])

# #Imprimir varias columnas

# print(df[["Nombre de la columna"],["Nombre de la columna"]])


# # Filtrar filas

# print(df[df["Age"]>25])

# # Seleccionar por una posición particular

# #obtener la primera fila por posición

# print(df.iloc[0])

# #obtener la primera columna por posición

# print(df.iloc[:,0])

# # Seleccionar por etiqueta

# # Imprimir la primera fila por etiqueta de indice
# print(df.loc[0])

# # Imprimir la primera columna por etiqueta de indice
# print(df.loc[:,"Nombre de la columna"])





#-------------------------------------------------------
#Ejercicios propuestos

import pandas as pd

#https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv

# cargar dataset
df=pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

#explorar la estructura
#imprimir las primeras 5 filas
print("primeras 5 filas\n",df.head())

#imprimir las ultimas 5 filas
print("ultimas 5 filas\n",df.tail())

#obtener info del conjunto de datos
print("Información\n",df.info())

#obtener info estadistica del conjunto de datos
print("Información estadistica \n",df.describe())

# seleccionar columnas especificas
print("columnas especificas \n",df[['sepal_length','sepal_width']])

# filtrar datos de columnas
print("filtrado \n",df[(df['sepal_length']>5.0) & (df['species']=='setosa')])

#Encabezados

print('Encabezados\n',df.columns)

# Imprimir la columna 3

print('Imprimir tercera columna:\n',df.iloc[:,2])

# Imprimir por etiqueta de posición una columna

print('Imprimir por etiqueta de posición una columna:\n',df.loc[:,'species'])

# Imprimir por etiqueta de posición una fila

print('Imprimir por etiqueta de posición una fila:\n',df.loc[1])