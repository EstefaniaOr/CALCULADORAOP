# -*- coding: utf-8 -*-
"""
Created on Thu May  2 10:03:46 2019

@author: prestamour
"""
import random 

e = 2.71828

def montecarlo(num_ejemplos=10000):
    """Esta función realiza un montacarlo inicial con 10000 iteraciones"""
    sum_ejemplos = 0
    for i in range(num_ejemplos):
        x = random.gauss(0,1) #método .gauss es más rápido que .normalvariate
        y = (e**(-1*x))/(1+(x-1)**2) 
        sum_ejemplos += y

    return float(sum_ejemplos/num_ejemplos)
    
print(montecarlo())

# https://docs.python.org/3/library/random.html
# El rango siempre va a ser entre 0 y 1 luego se pueden eliminar el rango.