'''
1- Aplicar analisis exploratorio y visualización de datos(EDA-Exploratory Data Analysis o Análisis Exploratorio de Datos.)
    -EDA: El analisis exploratorio de datos implica resumir 
    conjuntos de datos apra descubir patrones y relaciones y conocimientos,
    Los pasos en EDA incluyen:
        -Limpieza de datos: Manejar valoreos faltantes, eliminar duplicados y corregir inconsistencias
        -Transformación de datos:Cmabiar tipos de datos,Normalizar datos y crear nuevas caracteristicas
        -Agregación y filtrado: Resumir datos y aplicar filtros para centrarse en aspectos especificos
'''

# Como identificar patrones, tendencias y correlaciones
'''
Algunas herramientas visuales que se utilizan para estos analisis:
    -Graficois de lineas: Para datos de tendencias a lo largo del tiempo
    -Grafico de barras: Para comparaciones categorizadas
    -Diagramas de disperción: Para encontrar relaciones
    -Mapas de calor: Para el analisis de correlación
'''

# Patrones clave que se esta buscando:
''''
-Relaciones entre variables(Correlaciones)
-Distribución de variables (Histogramas y Diagramas de caja)
-Valores atipicos y anomalias ()
'''

# Estadisticas resumidas, conocimientos visuales y generación de hipotesis

#Estadisticas resumidas
''''
Se pueden obtener mediante un marco de datos y llamar a la función describe que proporcionara
la media, la desviación estandar, los valores minimos y maximos...etc.
'''

#conocimientos visuales
''''
Por ejemplo cuando se utiliza .correlation de seaborn que proporciona una matriz de correlación
'''

#generación de hipotesis
''''
Formulación de hipotesis basadas en observaciones, Normalmente se utiliza EDA para analizar
o refutar hipotesis
'''

#----------------------------------Ejercicio practico----------------------------------------

#1- Realizar limpieza de datos, agregación y filtrado

import pandas as pd

# dataset de titanic
df=pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
#print(df)

#Inpeccionar los datos
print(df.info())
print(df.describe())

# Manejar valores faltantes

#Rellenar edades faltantes con la media
df["Age"]=df["Age"].fillna(df["Age"].median())

# Enbarke
df["Embarked"]=df["Embarked"].fillna(df["Embarked"].mode()[0]) # Devuelve la primera moda

# Eliminar duplicados
df=df.drop_duplicates()

#Filtrar datos: pasajeros en prmiera clase

first_class=df[df["Pclass"]==1]
print("Pasajeros en primera clase\n",first_class.head())

#-------- Crear visualizaciones para tendencias

import matplotlib.pyplot as plt
import seaborn as sns

# Mostrar grafico de barras (tasa de supervivencia por clase)

SupervivenciaPorClase=df.groupby("Pclass")["Survived"].mean()
''''
df.groupby("Pclass")
→ agrupa el DataFrame por la columna Pclass (la clase del boleto: 1ª, 2ª o 3ª).

["Survived"]
→ selecciona la columna Survived (0 = no sobrevivió, 1 = sobrevivió).

.mean()
→ calcula el promedio de Survived para cada clase.
'''
SupervivenciaPorClase.plot(kind="bar",color="skyblue")
plt.title("tasa de supervivencia por clase")
plt.xlabel("clase")
plt.ylabel("tasa de supervivencia")
plt.show()


#Histograma para ver cuanto es la distribución de edades

sns.histplot(df["Age"],kde=True, bins=20,color="purple")
plt.title('Distribución de edades')
plt.xlabel('Age')
plt.ylabel('Frecuency')
plt.show()

#Diagrama de disperción de edad vs tarifa

plt.scatter(df["Age"],df["Fare"],alpha=0.5,color='green')
plt.title('Edad vs Tarifa')
plt.xlabel('Edad')
plt.ylabel('fare')
plt.show()


#Identificar patrones y anomalias

# Las personas de mayor clase tienen una tasa de supervivencia ams alta

# las personas mayores pagaron mas en tarifa

# Crear un informe que resuma las ideas

