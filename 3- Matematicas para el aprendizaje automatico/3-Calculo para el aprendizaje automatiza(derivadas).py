# Introducción a las derivadas y su papel en la optimización
'''
-Que son las derivadas?

Una derivada mide la tasa a la que una función cambia con respecto a su entrada 

    Para una función f(x) la derivada o tambien llamada f'(x) indica la pendiente 
    de la linea tangente en un punto x

- Rol de las derivadas en la optimización:
    las derivadas se utilizan para minimizar o maximizar una función lo dual es critico en el 
    aprendizaje automatico para automatizar funciones de perdida como por ejemplo:
        La función de perdida en la regresión lineal que mide el error 
        
        Las derivadas ayudan a encontrar la direccíón para ajustar los parametros 
        y minimizar este error

'''

# Como implementar derivadas en python

import sympy as sp

x=sp.Symbol('x')
f=x**2
derivada=sp.diff(f,x)

print('la derivada es: \n',derivada)

# Derivadas parciales

'''
Las derivadas parciales miden como cambia una funcíón con 
respecto a una variable mientras se mantiene constante la otra variable

    f(x,y)=x²+y²:

                    af/ax=2x, af/ay=2y

- Gradiante: Es un vector de todas las derivadas parciales, indicando la dirección
del ascense mas pronunciado para f de x igual a x al cuadrado mas y al cuadrado

    f(x,y)=x²+y² el gradiente es:

                    ▽f=[af/ax/af/ay]= |2x|
                                       |2y|
'''


x,y=sp.symbols('x y')
f=x**2+y**2
gradiante_x=sp.diff(f,x)
gradiante_y=sp.diff(f,y)

print('El gradiante de x es: \n',gradiante_x,' \n El gradiante de y es: \n',gradiante_y)


# Algoritmo de optimización de descenso de gradiente
''''
El descenso de gradiente es un algoritmo de optimización iterativo 
-utilizado para minimizar una función. Como por ejemplo una funcíón de perdida

-Actualiza los parametros en la dirección del gradiente negativo para encontrar el minimo
'''


#ejercicio

#1-Calcular derivadas basicas
x=sp.Symbol('x')
f=x**3-5*x+7
#calcular
derivada=sp.diff(f,x)
print(derivada)