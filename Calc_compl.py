"""Librerias utilizadas para el desarrollo de la Calculadora"""
from numpy import zeros, random, exp, amax, sqrt 
import tkinter as tk

"""Crear ventana"""     
     
def opcion_call():
    """Esta funcion crea la simulacion de la opcion call bajo el metodo de Montecarlo.
        Recrea una matriz en donde la primera columna son ceros y la segunda columna esta
        la funcion de pagos de la opcion y la aplica.Tambien depende del numero de iteraciones
        que se le incluyan.
        El maximo valor entre St-K o cero.
        Funcion de Pagos = MAX(St-K,0).
        Variables: St: Precio del Subyacente
                   K: Precio Strike
    """        
    option_data = zeros([int(iteraciones.get()), 2])
    rand = random.normal(0, 1, [1, int(iteraciones.get())])
    stock_price = float(assetprice.get())*exp(float(tiempo.get())*(float(rate.get()) - 0.5*float(volatility.get())**2)+float(volatility.get())*sqrt(float(tiempo.get()))*rand)
    option_data[:, 1] = stock_price - float(strikeprice.get())
    average = sum(amax(option_data, axis=1))/float(iteraciones.get())

    return var.set(exp(-1.0*float(rate.get())*float(tiempo.get()))*average)

def opcion_put():
    """Esta funcion crea la simulacion de la opcion put bajo el metodo de Montecarlo.
        Recrea una matriz en donde la primera columna son ceros y la segunda columna es
        la funcion de pagos de la opcion y la aplica.Tambien depende del numero de iteraciones
        que se le incluyan.
        El maximo valor entre K-St o cero.
        Funcion de Pagos = MAX(K-St,0).
        Variables: St: Precio del Subyacente
                   K: Precio Strike
    """        
    option_data = zeros([int(iteraciones.get()), 2])
    rand = random.normal(0, 1, [1, int(iteraciones.get())])
    stock_price = float(assetprice.get())*exp(float(tiempo.get())*(float(rate.get()) - 0.5*float(volatility.get())**2)+float(volatility.get())*sqrt(float(tiempo.get()))*rand)
    option_data[:, 1] = float(strikeprice.get()) - stock_price
    average = sum(amax(option_data, axis=1))/float(iteraciones.get())

    return var.set(exp(-1.0*float(rate.get())*float(tiempo.get()))*average)
    

def validar_valores_call ():
    """ Esta funcion genera las advertencias para el usuario en la opcion call,
     en caso que ingrese un valor no permitido dentro de los Textbox, para que 
     sepa que sus valores deben ser positivos en cada una de las casillas.
    """     
    if float(assetprice.get()) <= 0: 
        return var.set("El precio del activo debe ser un valor positivo")
    elif float(strikeprice.get()) <= 0:  
        return var.set("El precio Strike debe ser un valor positivo")
    elif float(tiempo.get()) <= 0:  
        return var.set("El tiempo debe ser un valor positivo")    
    elif int(iteraciones.get()) <= 0:  
        return var.set("El numero de iteraciones deben ser positivas")
    else:
        return opcion_call()
    
def validar_valores_put ():
    """ Esta funcion genera las advertencias para el usuario en la opcion call,
     en caso que ingrese un valor no permitido dentro de los Textbox, para que 
     sepa que sus valores deben ser positivos en cada una de las casillas.
    """     
    if float(assetprice.get()) <= 0: 
        return var.set("El precio del activo debe ser un valor positivo")
    elif float(strikeprice.get()) <= 0:  
        return var.set("El precio Strike debe ser un valor positivo")
    elif float(tiempo.get()) <= 0:  
        return var.set("El tiempo debe ser un valor positivo")    
    elif int(iteraciones.get()) <= 0:  
        return var.set("El numero de iteraciones deben ser positivas")
    else:
        return opcion_put()

"""Crea la ventana usando la libreria tkinter con las opciones especificadas."""      
ventana = tk.Tk()
ventana.title("Ventana")
ventana.geometry("580x600")
ventana.configure(background = "green")
var = tk.StringVar()

""" Son Las especificaciones de la ventana para que el usuario ingrese el 
    precio del activo subyacente, se definen los colores que se utilizan en 
    la interfaz, ademas toma el valor dado por el usuario para usarlo en el calculo.
"""   
assetprice = tk.Label(ventana, text = "Ingrese el Precio del Activo: ", bg = "black", fg = "white")
assetprice.pack(padx = 5, pady = 4, ipadx = 5, ipady = 5, fill = tk.X)
assetprice = tk.Entry(ventana)
assetprice.pack(fill = tk.X, padx = 5, pady = 5, ipadx = 5, ipady = 5)

""" Son Las especificaciones de la ventana para que el usuario ingrese el 
    precio Strike, se definen los colores que se utilizan en la interfaz, 
    ademas toma el valor dado por el usuario para usarlo en el calculo.
"""   
strikeprice = tk.Label(ventana, text = "Precio Strike: ", bg = "black", fg = "white")
strikeprice.pack(padx = 5, pady = 4, ipadx = 5, ipady = 5, fill = tk.X)
strikeprice = tk.Entry(ventana)
strikeprice.pack(fill = tk.X, padx = 5, pady = 5, ipadx = 5, ipady = 5)

""" Son Las especificaciones de la ventana para que el usuario ingrese la 
    volatilidad del activo subyacente, se definen los colores que se utilizan
    en la interfaz, ademas toma el valor dado por el usuario para usarlo en el calculo.
"""   
volatility = tk.Label(ventana, text = "Volatilidad: ", bg = "black", fg = "white")
volatility.pack(padx = 5, pady = 4, ipadx = 5, ipady = 5, fill = tk.X)
volatility = tk.Entry(ventana)
volatility.pack(fill = tk.X, padx = 5, pady = 5, ipadx = 5, ipady = 5)

""" Son Las especificaciones de la ventana para que el usuario ingrese la 
    tasa de interes, se definen los colores que se utilizan en la interfaz, 
    ademas toma el valor dado por el usuario para usarlo en el calculo.
"""   
rate = tk.Label(ventana, text = "Tasa de Interés: ", bg = "black", fg = "white")
rate.pack(padx = 5, pady = 4, ipadx = 5, ipady = 5, fill = tk.X)
rate = tk.Entry(ventana)
rate.pack(fill = tk.X, padx = 5, pady = 5, ipadx = 5, ipady = 5)

""" Son Las especificaciones de la ventana para que el usuario ingrese el 
    tiempo en años, se definen los colores que se utilizan en la interfaz, 
    ademas toma el valor dado por el usuario para usarlo en el calculo.
"""   
tiempo = tk.Label(ventana, text = "Tiempo: ", bg = "black", fg = "white")
tiempo.pack(padx = 5, pady = 4, ipadx = 5, ipady = 5, fill = tk.X)
tiempo = tk.Entry(ventana)
tiempo.pack(fill = tk.X, padx = 5, pady = 5, ipadx = 5, ipady = 5)

""" Son Las especificaciones de la ventana para que el usuario ingrese el 
   numero de iteraciones que desarrollara el programa, se definen los colores
   que se utilizan en la interfaz, ademas toma el valor dado por el usuario 
   para usarlo en el calculo.
"""   
iteraciones = tk.Label(ventana, text = "Iteraciones: ", bg = "black", fg = "white")
iteraciones.pack(padx = 5, pady = 4, ipadx = 5, ipady = 5, fill = tk.X)
iteraciones = tk.Entry(ventana)
iteraciones.pack(fill = tk.X, padx = 5, pady = 5, ipadx = 5, ipady = 5)

""" Crea  el boton para que la calculadora calcule el valor de la prima de la opcion Call.""" 
botoncalcularca = tk.Button(ventana, text = "Calcular opcion call", fg = "black", command = validar_valores_call )
botoncalcularca.pack(side = tk.TOP)

""" Crea  el boton para que la calculadora calcule el valor de la prima de la opcion Put.""" 
botoncalcularpu = tk.Button(ventana, text = "Calcular opcion put", fg = "black", command = validar_valores_put )
botoncalcularpu.pack(side = tk.TOP)

""" Imprime el resultado una vez se oprima e boton de la opcion de la cual se quiere saber su precio."""
res = tk.Label(ventana, bg = "plum", textvariable = var, padx = 5, pady = 5, width = 50)
res.pack()


ventana.mainloop()
