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
    
S0 = float(input("ingrese su Asset Price: " )) 
K = float(input("ingrese su Strike Price: " ))
T = float(input("ingrese su Tiempo: " ))
rf = float(input("ingrese su Free Rate: " ))
sigma = float(input("ingrese su Volatility: " ))
iteraciones = int(input("ingrese cuantas iteraciones desea: " ))

def validar_valores (objeto):
    if S0 <= 0: 
        return "su Asset Price debe ser un valor positivo"
    elif K <= 0:  
        return "su Strike Price debe ser un valor positivo"
    elif T <= 0:  
        return "su tiempo debe ser un valor positivo"    
    elif iteraciones <= 0:  
        return "sus iteraciones deben ser cantidades positivas"
    else:
        return objeto
        
def both_prices(objeto):
    if objeto != validar_valores(objeto):
        return validar_valores(objeto)
    else: 
        return "El precio de su opción put es {0} y el precio de su opción call es {1}".format(objeto.opcion_call(),objeto.opcion_put())
    
opcion1 = Option(S0, K, T, rf, sigma, iteraciones)
print(both_prices(opcion1))
