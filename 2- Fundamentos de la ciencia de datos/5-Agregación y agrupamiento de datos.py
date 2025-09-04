# # Funciones de agregación
# # --------------------------------------Agrupar datos por categorias:(uso de group by)--------------------------------------
# ''' Agrupar datos permite realizar operaciones en subconjuntos de datos basados en categorias 
# compartidas, esto mediante group by'''

# import pandas as pd

# grouped = pd.groupby("Nombre de la columna")


#     # Diferentes operaciones a travez de agrupar

#     #Iterar sobre grupos

# for name,group in grouped:
#     print(name)
#     print(group)

#     #Aplicar agregación

# grouped.mean()
# grouped.sum()


# # Funciones de agregación

# '''Primero se usa grouypby en donde se puede combinar la agrupación con metodos de agregación'''

# pd.groupby("columna de categoria")["Columna numerica"].mean()

# #Funcin de agregación para especificar la columna numerica y de alli especificar en formato de lista lo que se busca
# pd.groupby("categoria").agg({"Columna numerica": ["mean","max","min"]})

# # --------------------------------------uso de la tabla dinamica--------------------------------------

# # Se pueden reorganizar los datos con agregación si se usa la función de tabla dinamica

# pivot = pd.pivot_table(
#     values="Columna numerica",
#     index="Columna de categoria",
#     aggfunc="mean"
# )


# # --------------------------------------Agregación personalizada--------------------------------------
# #basicamente aplica funciones personalizadas

# def range_function(x):
#     return x.max() - x.min()

# pd.groupby("category_column")["numeric_column"].agg(range_function) 

# #Pasara los valores agrupando por la función personalizada


# # --------------------------------------Calcular estadisticas resumidas para datos agrupados--------------------------------------

# # Si se tienen datos agrupados se obtienen las estadisticas con:

# # Estadisticas comunes que se pueden obtener: 
#     #-mean
#     #-max
#     #-min

# pd.groupby("category_column")["numeric_column"].mean()
# pd.groupby(",ategory_column")["numeric_column"].max()
# pd.groupby("category_column")["numeric_column"].min()


# # --------------------------------------Hacer una agregación multiple--------------------------------------

# #Agrupar por multiagregación 

# pd.groupby("category_column").agg(
#     {"numeric_column":["mean","max","min"]}
#     )


#--------------------------------------Ejercicio 1:--------------------------------------

import pandas as pd

# Agrupar datos por una columna categorica

data ={
    "Class":["A","B","A","B","C","C"],
    "Score":[85,90,88,72,95,90],
    "Age":[15,16,15,17,16,15]
}

df=pd.DataFrame(data)

print("- Marco de datos original; \n",df)

groped=df.groupby('Class').mean()

print("- Marco de datos agrupado: \n",groped)


#--------------------------------------Ejercicio 2:--------------------------------------

# Calcular las estadisticas resumidas para datos agrupados

stats=df.groupby('Class').agg({
    "Score":["mean","min","max"],
    "Age":["mean","min","max"]
})


# # Funciones de agregación
# # --------------------------------------Agrupar datos por categorias:(uso de group by)--------------------------------------
# ''' Agrupar datos permite realizar operaciones en subconjuntos de datos basados en categorias 
# compartidas, esto mediante group by'''

# import pandas as pd

# grouped = pd.groupby("Nombre de la columna")


#     # Diferentes operaciones a travez de agrupar

#     #Iterar sobre grupos

# for name,group in grouped:
#     print(name)
#     print(group)

#     #Aplicar agregación

# grouped.mean()
# grouped.sum()


# # Funciones de agregación

# '''Primero se usa grouypby en donde se puede combinar la agrupación con metodos de agregación'''

# pd.groupby("columna de categoria")["Columna numerica"].mean()

# #Funcin de agregación para especificar la columna numerica y de alli especificar en formato de lista lo que se busca
# pd.groupby("categoria").agg({"Columna numerica": ["mean","max","min"]})

# # --------------------------------------uso de la tabla dinamica--------------------------------------

# # Se pueden reorganizar los datos con agregación si se usa la función de tabla dinamica

# pivot = pd.pivot_table(
#     values="Columna numerica",
#     index="Columna de categoria",
#     aggfunc="mean"
# )


# # --------------------------------------Agregación personalizada--------------------------------------
# #basicamente aplica funciones personalizadas

# def range_function(x):
#     return x.max() - x.min()

# pd.groupby("category_column")["numeric_column"].agg(range_function) 

# #Pasara los valores agrupando por la función personalizada


# # --------------------------------------Calcular estadisticas resumidas para datos agrupados--------------------------------------

# # Si se tienen datos agrupados se obtienen las estadisticas con:

# # Estadisticas comunes que se pueden obtener: 
#     #-mean
#     #-max
#     #-min

# pd.groupby("category_column")["numeric_column"].mean()
# pd.groupby(",ategory_column")["numeric_column"].max()
# pd.groupby("category_column")["numeric_column"].min()


# # --------------------------------------Hacer una agregación multiple--------------------------------------

# #Agrupar por multiagregación 

# pd.groupby("category_column").agg(
#     {"numeric_column":["mean","max","min"]}
#     )


#--------------------------------------Ejercicio 1:--------------------------------------

import pandas as pd

# Agrupar datos por una columna categorica

data ={
    "Class":["A","B","A","B","C","C"],
    "Score":[85,90,88,72,95,90],
    "Age":[15,16,15,17,16,15]
}

df=pd.DataFrame(data)

print("- Marco de datos original; \n",df)

groped=df.groupby('Class').mean()

print("- Marco de datos agrupado: \n",groped)


#--------------------------------------Ejercicio 2:--------------------------------------

# Calcular las estadisticas resumidas para datos agrupados

stats=df.groupby('Class').agg({
    "Score":["mean","min","max"],
    "Age":["mean","min","max"]
})


print("- Estadisticas: \n",stats)