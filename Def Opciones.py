import numpy as np

class OptionPricing:
    def __init__(self, S0, K, T, rf, sigma, iteration):
        """Option Pricing representa los valores necesarios para calcular
            el valor de la opción que se está buscando"""
        self.S0 = S0
        self.K = K
        self.T = T
        self.rf = rf
        self.sigma = sigma
        self.iteration = iteration
    
    def call_option_simulation(self):
        """Es la simulación de la opcion Call bajo el metodo de Monte Carlo"""        
        option_data = np.zeros([self.iteration, 2])
        rand = np.random.normal(0, 1, [1, self.iteration])
        stock_price = self.S0*np.exp(self.T*(self.rf - 0.5*self.sigma**2)+self.sigma*np.sqrt(self.T)*rand)
        option_data[:, 1] = stock_price - self.K
        average = np.sum(np.amax(option_data, axis=1))/float(self.iteration)

        return np.exp(-1.0*self.rf*self.T)*average
    
    def put_option_simulation(self):
        option_data = np.zeros([self.iteration, 2])
        rand = random.gauss(0, 1, [1, self.iteration])
        stock_price = self.S0*np.exp(self.T*(self.rf - 0.5*self.sigma**2)+self.sigma*np.sqrt(self.T)*rand)
        option_data[:, 1] = self.K - stock_price
        average = np.sum(np.amax(option_data, axis=1))/float(self.iteration)

        return np.exp(-1.0*self.rf*self.T)*average
    
