# import pandas as pd

# # limpieza y preparación de datos

# #-------------------------Asegurarse de que los datos esten limpios-------------------------------------

# # Manejo de valores faltantres

# '''¿Por que manejar los datos faltantes?

# Los datos falantes pueden afectar el analisis y el rendimiento del modelo,
# pandas propoirciona herramientas poderosas para gestionar los datos faltantes
# ''' 

# # Existen diferentes metodos:

# # 1- Eliminar los valores faltantes
# #Ejemplo:

# df=pd.read_excel('')
# df=df.dropna() # Eliminara cualquier fila con valores faltantes

# # Eliminar columnas con valores faltantes o que no son necesarias

# df=df.dropna(axis=1)# Eliminara columnas con valores faltantes

# # 2- Rellenar los valores faltantes
# #Ejemplo:

# df["Column_name"]=df["Column_name"].fillna("valor ya sea numerico o e texto")

# #tipos de relleno

# #añadir valores basados en datos disponibles hacia adelante
# df.fillna(method="ffill")
# #añadir valores basados en datos disponibles hacia atras
# df.fillna(method="bfill")

# # 3- Interpoloación lineal donde basandose en datos que se tienen se pueden llenar 
# # datos que estan en lineas similares a ese conjunto de datos en particular 
# #Ejemplo:

# df["column_name"]=df["column_name"].interpolate() # Esto agregara valores basados en la interpolación

# #-------------------------Transformación de datos-------------------------------------

# # Renombrar columnas
# #Ejemplo:

# df=df.rename(columns={"old_name":"new_name"})

# # cambiar tipos de datos
# #Ejemplo:
# df["Column_name"]=df["Column_name"].astype("Tipo de dato a cambiar")
# #Ejmplo convertir una cadena a fecha y hora
# df["Column_name"]=pd.to_datetime(df["Column_name"])

# # Creación o modificación de columnas
# #Ejemplo:
# df["new_columnn"] = df["existing_column"]*2


# #-------------------------Combinar y fucionar marcos de datos-------------------------------------

# #Concatenación(Concatenation): Combinara marcos de datos a lo largo de filas o columnas
# #Ejemplo:

# df1=pd.read_excel("Ubicación")
# df2=pd.read_excel("Ubicación")

# combinar=pd.concat([df1,df2], axis=0)# Combinar desde el eje filas

# combinar=pd.concat([df1,df2], axis=1)# Combinar desde el eje columnas

# #fusion(Merging): Fusionara marcos de datos basandose en una clave o condición

# merged = pd.merge(df1,df2,on="Columna_comun_en_marcos_de_datos")

# merged = pd.merge(df1,df2,how="Left",on="Columna_comun_en_marcos_de_datos") # unión desde la izquierda

# merged = pd.merge(df1,df2,how="inner",on="Columna_comun_en_marcos_de_datos") # unión interna

# #Unir(joining): Une los marcos de datos uzando la alineación de indices

# joined=df1.join(df2,how="inner") # se puede inner o left



# ---------------------------------------Ejercicio--------------------------------------------

# import pandas as pd
# import numpy as np

# # crear un conjunto de datos de muestra

# data={
#     "Name":["Alice","BOb",np.nan,"David"],
#     "Age":[25,np.nan,30,35],
#     "Score":[85,90,np.nan,88]
# }

# df=pd.DataFrame(data)

# print("Dataframe Original \n",df)

# #rellenar valores vacios basandoce en la media de las diferentes columnas

# df["Age"]=df["Age"].fillna(df["Age"].mean())

# df["Score"]=df["Score"].interpolate()

# print("dataset sin espacios en blanco\n", df)

# # renombrar columnas

# df=df.rename(columns={"Name":"Student_Name","Score":"Exam_score"})

# print("Cambio de nombre\n", df)


#Ejercicio 2:

# Fucionar dos conjuntos de datos y realizar una transformación de datos
import pandas as pd
import numpy as np

df1=pd.DataFrame({
    "ID":[1,2,3],
    "Name":["Alice","Bob","Charlie"],
    "Age":[25,30,35]
})

df2=pd.DataFrame({
    "ID":[1,2,3],
    "score":[85,90,88],
})

print("Conjunto 1 \n",df1)

print("Conjunto 2 \n",df2)

merged=pd.merge(df1,df2,on="ID")

print("Dataframe fusionado: \n",merged)