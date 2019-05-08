import numpy as np

class Option:
    def __init__(self, S0, K, T, rf, sigma, iteraciones):
        """Option Pricing representa los valores necesarios para calcular
            el valor de la opción que se está buscando"""
        self.S0 = S0
        self.K = K
        self.T = T
        self.rf = rf
        self.sigma = sigma
        self.iteraciones = iteraciones
    
    def opcion_call(self):
        """Es la simulación de la opcion Call bajo el metodo de Monte Carlo"""        
        option_data = np.zeros([self.iteraciones, 2])
        rand = np.random.normal(0, 1, [1, self.iteraciones])
        stock_price = self.S0*np.exp(self.T*(self.rf - 0.5*self.sigma**2)+self.sigma*np.sqrt(self.T)*rand)
        option_data[:, 1] = stock_price - self.K
        average = np.sum(np.amax(option_data, axis=1))/float(self.iteraciones)

        return np.exp(-1.0*self.rf*self.T)*average
    
    def opcion_put(self):
        """Esta es la simulación de la opcion Put bajo el metodo de Monte Carlo""" 
        option_data = np.zeros([self.iteraciones, 2])
        rand = np.random.normal(0, 1, [1, self.iteraciones])
        stock_price = self.S0*np.exp(self.T*(self.rf - 0.5*self.sigma**2)+self.sigma*np.sqrt(self.T)*rand)
        option_data[:, 1] = self.K - stock_price
        average = np.sum(np.amax(option_data, axis=1))/float(self.iteraciones)

        return np.exp(-1.0*self.rf*self.T)*average
    
S0 = float(input("ingrese su S0: " )) 
K = float(input("ingrese su K: " ))
T = float(input("ingrese su T: " ))
rf = float(input("ingrese su rf: " ))
sigma = float(input("ingrese su sigma: " ))
iteraciones = int(input("ingrese cuantas iteraciones desea: " ))

opcion1 = Option(S0, K, T, rf, sigma, iteraciones)
print("Precio de la opcion call : ", opcion1.opcion_call())
print("Precio de la opcion put: ", opcion1.opcion_put())    
