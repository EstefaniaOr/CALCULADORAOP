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
        option_data = zeros([int(iteraciones.get()), 2])
        rand = random.normal(0, 1, [1, int(iteraciones.get())])
        stock_price = float(assetprice.get())*exp(float(tiempo.get())*(float(rate.get()) - 0.5*float(volatility.get())**2)+float(volatility.get())*sqrt(float(tiempo.get()))*rand)
        option_data[:, 1] = stock_price - float(strikeprice.get())
        average = sum(amax(option_data, axis=1))/float(iteraciones.get())

        return var.set(exp(-1.0*float(rate.get())*float(tiempo.get()))*average)

def opcion_put():
        """Esta es la simulación de la opcion Put bajo el metodo de Monte Carlo""" 
        option_data = zeros([int(iteraciones.get()), 2])
        rand = random.normal(0, 1, [1, int(iteraciones.get())])
        stock_price = float(assetprice.get())*exp(float(tiempo.get())*(float(rate.get()) - 0.5*float(volatility.get())**2)+float(volatility.get())*sqrt(float(tiempo.get()))*rand)
        option_data[:, 1] = float(strikeprice.get()) - stock_price
        average = sum(amax(option_data, axis=1))/float(iteraciones.get())

        return var.set(exp(-1.0*float(rate.get())*float(tiempo.get()))*average)
    
def validar_valores_call ():
    if float(assetprice.get()) <= 0: 
        return var.set("su assetprice debe ser un valor positivo")
    elif float(strikeprice.get()) <= 0:  
        return var.set("su strikeprice debe ser un valor positivo")
    elif float(tiempo.get()) <= 0:  
        return var.set("su tiempo debe ser un valor positivo")    
    elif int(iteraciones.get()) <= 0:  
        return var.set("sus iteraciones deben ser caantidades positivas")
    else:
        return opcion_call()
    
def validar_valores_put ():
    if float(assetprice.get()) <= 0: 
        return var.set("su assetprice debe ser un valor positivo")
    elif float(strikeprice.get()) <= 0:  
        return var.set("su strikeprice debe ser un valor positivo")
    elif float(tiempo.get()) <= 0:  
        return var.set("su tiempo debe ser un valor positivo")    
    elif int(iteraciones.get()) <= 0:  
        return var.set("sus iteraciones deben ser caantidades positivas")
    else:
        return opcion_put()
                       
ventana = tk.Tk()
ventana.title("Ventana")
ventana.geometry("580x600")
ventana.configure(background = "green")
var = tk.StringVar()

e1 = tk.Label(ventana, text = "ingrese su Asset Price: ", bg = "black", fg = "white")
e1.pack(padx = 5, pady = 4, ipadx = 5, ipady = 5, fill = tk.X)
assetprice = tk.Entry(ventana)
assetprice.pack(fill = tk.X, padx = 5, pady = 5, ipadx = 5, ipady = 5)

e2 = tk.Label(ventana, text = "Strike Price: ", bg = "black", fg = "white")
e2.pack(padx = 5, pady = 4, ipadx = 5, ipady = 5, fill = tk.X)
strikeprice = tk.Entry(ventana)
strikeprice.pack(fill = tk.X, padx = 5, pady = 5, ipadx = 5, ipady = 5)

e3 = tk.Label(ventana, text = "Volatility: ", bg = "black", fg = "white")
e3.pack(padx = 5, pady = 4, ipadx = 5, ipady = 5, fill = tk.X)
volatility = tk.Entry(ventana)
volatility.pack(fill = tk.X, padx = 5, pady = 5, ipadx = 5, ipady = 5)

e4 = tk.Label(ventana, text = "Rate: ", bg = "black", fg = "white")
e4.pack(padx = 5, pady = 4, ipadx = 5, ipady = 5, fill = tk.X)
rate = tk.Entry(ventana)
rate.pack(fill = tk.X, padx = 5, pady = 5, ipadx = 5, ipady = 5)

e5 = tk.Label(ventana, text = "Tiempo: ", bg = "black", fg = "white")
e5.pack(padx = 5, pady = 4, ipadx = 5, ipady = 5, fill = tk.X)
tiempo = tk.Entry(ventana)
tiempo.pack(fill = tk.X, padx = 5, pady = 5, ipadx = 5, ipady = 5)

e6 = tk.Label(ventana, text = "Iteraciones: ", bg = "black", fg = "white")
e6.pack(padx = 5, pady = 4, ipadx = 5, ipady = 5, fill = tk.X)
iteraciones = tk.Entry(ventana)
iteraciones.pack(fill = tk.X, padx = 5, pady = 5, ipadx = 5, ipady = 5)

botoncalcularca = tk.Button(ventana, text = "Calcular opcion call", fg = "black", command = validar_valores_call )
botoncalcularca.pack(side = tk.TOP)

botoncalcularpu = tk.Button(ventana, text = "Calcular opcion put", fg = "black", command = validar_valores_put )
botoncalcularpu.pack(side = tk.TOP)

res = tk.Label(ventana, bg = "plum", textvariable = var, padx = 5, pady = 5, width = 50)
res.pack()


ventana.mainloop()
