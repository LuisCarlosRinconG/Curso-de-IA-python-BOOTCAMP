# Graficar datos

# introducción a matplotli
'''Es una bibliotecqa fundamental de python para crear graficos estaticos 
interactivos y animados, Permite una personalización detallada de los graficos'''

import matplotlib.pyplot as plt

# grafico basico
# x=[1,2,3,4]
# y=[10,20,25,30]
# plt.plot(x,y)
# plt.show()

# graficos basicos:

# Grafico de lineas(Line Plot): utilizado para visualizar tendencias o secuencias a lo largo del tiempo

# plt.plot([40,50,26,86],[45,82,59,84])
# plt.title("Line Plot")
# plt.xlabel("Eje X")
# plt.ylabel("Eje Y")
# plt.legend()
# plt.show()

# Grafico de barras(Bar Chart): Se utiliza para datos categoricos 

# categories=["A","B","C"]

# values=[10,15,7]
# plt.bar(categories,values,color="Blue")
# plt.title("Bar Chart")
# plt.show()

# Histograma(Histograma): Muestra la distribucióbn de un conjunto de datos 

# data=[1,2,2,3,3,3,4,4,4,4]
# plt.hist(data,bins=4,color="green",edgecolor='black')
# plt.title("Histograma")
# plt.show()

# Diagrama de disperción(scatter plot): Visualiza la relación entre dos varialbes continuas y se 
#utiliza mucho en proyectos de IA

# x=[1,2,3,4,5]
# y=[10,12,25,30,45]
# plt.scatter(x,y,color="red")
# plt.title("Scatter plot")
# plt.show()

#-----------------------------------Persanalización de graficos--------------------------------------

''''
- Se pueden agregar titulos, etiquetas de eje, leyendas
'''

# - Se puede ajustar colores y estilos

# x=[1,2,3,4,5]
# y=[10,12,25,30,45]
# plt.plot(x,y, label="Trend", color="orange",linestyle='-.',marker='x')
# plt.title("Scatter plot")
# plt.xlabel("Eje X")
# plt.ylabel("Eje Y")
# plt.legend(["Dataset 1"])
# plt.show()





#_________________Introducción a seaborn para visualizaciones avanzadas_________________

'''
Construido sobre matplotlib para graficos mas faciles y visualmente atractivos,
seaborn nacio para traer mas personalizaciones a matplotlib, proporciona interfaces de 
alto nmivel para graficos estadisticos:
    - Mapa de calor(Heatmap): Visualiza un matriz de datos
    - grafico de pares(Pairplot): Muestra la relación por pares en conjuntos de datos 
'''

import seaborn as sns # libreria de seabron

import numpy as np
#Mapa de calor(Heatmap): Visualiza un matriz de datos
# data =np.random.rand(5,5)
# sns.heatmap(data,annot=True,cmap="coolwarm") # cmap es el color 
# plt.title("Heatmap")
# plt.show()


# Grafico de pares(Pairplot): Muestra la relación por pares en conjuntos de datos 
# import pandas as pd
# data =np.random.rand(100,5)
# df=pd.DataFrame(data,columns=["A","B","C","D","E"])
# sns.pairplot(df)
# plt.show()


#-----------------------------Ejercicios-------------------------

#Ejercicio 1:  Trazar un graficos de lineas, de barras y un diagrama de disperción

# Line plot

years=[2010,2011,2012,2013]
sales=[100,120,140,160]
plt.plot(years,sales,label='Sales Trend',color='blue',marker='o')
plt.title("Sales over Years")
plt.xlabel("Years")
plt.ylabel("Sales")
plt.legend()
plt.show()

# Bar Chart
categories=["Electronics","clothing","Groceries"]
revenue=[250,400,150]
plt.bar(categories,revenue,color="green")
plt.title("Revenue by category")
plt.show()

# Scatter plot

hours_studied=[1,2,3,4,5]
exam_scores=[50,55,65,70,85]

plt.scatter(hours_studied,exam_scores, color="red")
plt.title("study hours vs Exam Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Scores")
plt.show()

# Ejercicio 2: Crear una mapa de calor atravez de una matriz de correlación
import pandas as pd

data=pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

del data['species']

# Calcular la matriz de la estructura completa
correlation_matrix=data.corr()

# Graficar mapa de calor
sns.heatmap(correlation_matrix, annot=True,cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
