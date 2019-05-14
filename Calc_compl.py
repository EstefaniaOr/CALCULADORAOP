#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 16:59:26 2019

@author: lovelace
"""

from numpy import zeros, random, exp, amax, sqrt 
import tkinter as tk

"""Crear ventana"""     
     
def opcion_call():
        """Es la simulación de la opcion Call bajo el metodo de Monte Carlo"""        
        option_data = zeros([int(entrada6.get()), 2])
        rand = random.normal(0, 1, [1, int(entrada6.get())])
        stock_price = float(entrada1.get())*exp(float(entrada5.get())*(float(entrada4.get()) - 0.5*float(entrada3.get())**2)+float(entrada3.get())*sqrt(float(entrada5.get()))*rand)
        option_data[:, 1] = stock_price - float(entrada2.get())
        average = sum(amax(option_data, axis=1))/float(entrada6.get())

        return var.set(exp(-1.0*float(entrada4.get())*float(entrada5.get()))*average)

def opcion_put():
        """Esta es la simulación de la opcion Put bajo el metodo de Monte Carlo""" 
        option_data = zeros([int(entrada6.get()), 2])
        rand = random.normal(0, 1, [1, int(entrada6.get())])
        stock_price = float(entrada1.get())*exp(float(entrada5.get())*(float(entrada4.get()) - 0.5*float(entrada3.get())**2)+float(entrada3.get())*sqrt(float(entrada5.get()))*rand)
        option_data[:, 1] = float(entrada2.get()) - stock_price
        average = sum(amax(option_data, axis=1))/float(entrada6.get())

        return var.set(exp(-1.0*float(entrada4.get())*float(entrada5.get()))*average)
    
def validar_valores_call ():
    if float(entrada1.get()) <= 0: 
        return var.set("su S0 debe ser un valor positivo")
    elif float(entrada2.get()) <= 0:  
        return var.set("su S0 debe ser un valor positivo")
    elif float(entrada5.get()) <= 0:  
        return var.set("su S0 debe ser un valor positivo")    
    elif int(entrada6.get()) <= 0:  
        return var.set("sus iteraciones deben ser caantidades positivas")
    else:
        return opcion_call()
    
def validar_valores_put ():
    if float(entrada1.get()) <= 0: 
        return var.set("su S0 debe ser un valor positivo")
    elif float(entrada2.get()) <= 0:  
        return var.set("su S0 debe ser un valor positivo")
    elif float(entrada5.get()) <= 0:  
        return var.set("su S0 debe ser un valor positivo")    
    elif int(entrada6.get()) <= 0:  
        return var.set("sus iteraciones deben ser caantidades positivas")
    else:
        return opcion_put()
                       
ventana = tk.Tk()
ventana.title("Ventana")
ventana.geometry("580x600")
ventana.configure(background = "blue")
var = tk.StringVar()

e1 = tk.Label(ventana, text = "ingrese su Asset Price: ", bg = "black", fg = "white")
e1.pack(padx = 5, pady = 4, ipadx = 5, ipady = 5, fill = tk.X)
entrada1 = tk.Entry(ventana)
entrada1.pack(fill = tk.X, padx = 5, pady = 5, ipadx = 5, ipady = 5)

e2 = tk.Label(ventana, text = "Strike Price: ", bg = "black", fg = "white")
e2.pack(padx = 5, pady = 4, ipadx = 5, ipady = 5, fill = tk.X)
entrada2 = tk.Entry(ventana)
entrada2.pack(fill = tk.X, padx = 5, pady = 5, ipadx = 5, ipady = 5)

e3 = tk.Label(ventana, text = "Volatility: ", bg = "black", fg = "white")
e3.pack(padx = 5, pady = 4, ipadx = 5, ipady = 5, fill = tk.X)
entrada3 = tk.Entry(ventana)
entrada3.pack(fill = tk.X, padx = 5, pady = 5, ipadx = 5, ipady = 5)

e4 = tk.Label(ventana, text = "Rate: ", bg = "black", fg = "white")
e4.pack(padx = 5, pady = 4, ipadx = 5, ipady = 5, fill = tk.X)
entrada4 = tk.Entry(ventana)
entrada4.pack(fill = tk.X, padx = 5, pady = 5, ipadx = 5, ipady = 5)

e5 = tk.Label(ventana, text = "Tiempo: ", bg = "black", fg = "white")
e5.pack(padx = 5, pady = 4, ipadx = 5, ipady = 5, fill = tk.X)
entrada5 = tk.Entry(ventana)
entrada5.pack(fill = tk.X, padx = 5, pady = 5, ipadx = 5, ipady = 5)

e6 = tk.Label(ventana, text = "Iteraciones: ", bg = "black", fg = "white")
e6.pack(padx = 5, pady = 4, ipadx = 5, ipady = 5, fill = tk.X)
entrada6 = tk.Entry(ventana)
entrada6.pack(fill = tk.X, padx = 5, pady = 5, ipadx = 5, ipady = 5)

botoncalcularca = tk.Button(ventana, text = "Calcular opcion call", fg = "black", command = validar_valores_call )
botoncalcularca.pack(side = tk.TOP)

botoncalcularpu = tk.Button(ventana, text = "Calcular opcion put", fg = "black", command = validar_valores_put )
botoncalcularpu.pack(side = tk.TOP)

res = tk.Label(ventana, bg = "plum", textvariable = var, padx = 5, pady = 5, width = 50)
res.pack()


ventana.mainloop()