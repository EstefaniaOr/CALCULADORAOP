import random 
import math
import numpy as np


e = 2.71828

def create_numbers ():
    """ Esta función sirve para generar números aleatorios entre 0 y 1""" 
    rng=random.Random()
    numbers = []
    for  i in range(10000-1):
        num = rng.random()
        numbers += [num]
    return numbers

print (create_numbers())


def get_rand_number(val_min, val_max):
    """Esta función genera números aleatorios utilizando una distribución
    uniforme para que todos tengas igual probabilidad entre dos valores
    asignados"""
    range = val_max - val_min
    elecc = random.normalvariate(0,1)
    return val_min + range*elecc

def f_de_x(x):
    return(e**(-1*x))/(1+(x-1)**2)

def first_montecarlo(num_ejemplos=10000):
    """Esta función realiza un montacarlo inicial, probando que funcione
    el método"""
    limite_inferior = 0
    limite_superior = 1
   
    sum_ejemplos = 0
    for i in range(num_ejemplos):
        x = get_rand_number(limite_inferior, limite_superior)
        sum_ejemplos += f_de_x(x)

    return (limite_superior - limite_inferior) * float(sum_ejemplos/num_ejemplos)
    
print(first_montecarlo())

