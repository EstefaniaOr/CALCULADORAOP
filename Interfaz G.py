import tkinter as tk

ventana = tk.Tk()
ventana.title("Ventana")
ventana.geometry("580x580")
ventana.configure(background = "blue")
var = tk.StringVar()

e1 = tk.Label(ventana, text = "Asset Price: ", bg = "black", fg = "white")
e1.pack(padx = 5, pady = 4, ipadx = 5, ipady = 5, fill = tk.X)
entrada1 = tk.Entry(ventana)
entrada1.pack(fill = tk.X, padx = 5, pady = 5, ipadx = 5, ipady = 5)

e2 = tk.Label(ventana, text = "Strike Price: ", bg = "black", fg = "white")
e2.pack(padx = 5, pady = 4, ipadx = 5, ipady = 5, fill = tk.X)
entrada1 = tk.Entry(ventana)
entrada1.pack(fill = tk.X, padx = 5, pady = 5, ipadx = 5, ipady = 5)

e3 = tk.Label(ventana, text = "Volatility: ", bg = "black", fg = "white")
e3.pack(padx = 5, pady = 4, ipadx = 5, ipady = 5, fill = tk.X)
entrada1 = tk.Entry(ventana)
entrada1.pack(fill = tk.X, padx = 5, pady = 5, ipadx = 5, ipady = 5)

e4 = tk.Label(ventana, text = "Rate: ", bg = "black", fg = "white")
e4.pack(padx = 5, pady = 4, ipadx = 5, ipady = 5, fill = tk.X)
entrada1 = tk.Entry(ventana)
entrada1.pack(fill = tk.X, padx = 5, pady = 5, ipadx = 5, ipady = 5)

e5 = tk.Label(ventana, text = "Time: ", bg = "black", fg = "white")
e5.pack(padx = 5, pady = 4, ipadx = 5, ipady = 5, fill = tk.X)
entrada1 = tk.Entry(ventana)
entrada1.pack(fill = tk.X, padx = 5, pady = 5, ipadx = 5, ipady = 5)

e6 = tk.Label(ventana, text = "Iterations: ", bg = "black", fg = "white")
e6.pack(padx = 5, pady = 4, ipadx = 5, ipady = 5, fill = tk.X)
entrada1 = tk.Entry(ventana)
entrada1.pack(fill = tk.X, padx = 5, pady = 5, ipadx = 5, ipady = 5)

botoncalcular = tk.Button(ventana, text = "Calcular", fg = "black" )
botoncalcular.pack(side = tk.TOP)

res = tk.Label(ventana, bg = "plum", textvariable = var, padx = 5, pady = 5, width = 50)
res.pack()



ventana.mainloop()
