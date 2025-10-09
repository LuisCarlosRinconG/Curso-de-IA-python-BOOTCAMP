#integrales
'''
las integrales calculan el area bajo una curva representando toda la acumulación 
que esta bajo la curva
'''

# Aplicaciones en ML

'''
-Distribución de probabilidad: Las integrales se utilizan para calcular la probabilidad bajo
una función de dencidad de probabilidad,
-Funciones de costo
'''

import sympy as sp

x=sp.Symbol('x')
f=x**2
definite_integral=sp.integrate(f,(x,0,2))
indefinite_integral=sp.integrate(f,x)

print(definite_integral)

print(indefinite_integral)




#Conceptos de optimizaciones

'''
*minimos locales vs Globales
    minimo local: Es un punto donde la función tiene un valor mas bajo que los puntos del vecindario
    minimo global: Es el punto mas bajo absoluto de la función

'''