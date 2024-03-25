import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

class SerieTemporalARIMA:
    def __init__(self, data, order=(1,1,1)):
        """
        Inicializa la instancia de la clase con los datos y el orden del modelo ARIMA.
        
        :param data: DataFrame de Pandas con dos columnas: 'Year' y la variable de interés.
        :param order: Una tupla (p, d, q) que representa el orden del modelo ARIMA.
        """
        self.data = data
        self.order = order
        self.model = None
        self.result = None

    def preprocess_data(self):
        """
        Preprocesa los datos: establece 'Year' como índice y ordena el DataFrame.
        """
        self.data.set_index("Year", inplace=True)
        self.data.sort_index(inplace=True)

    def plot_data(self):
        """
        Visualiza la serie temporal.
        """
        plt.figure(figsize=(10, 6))
        plt.plot(self.data, marker='o', linestyle='-')
        plt.xlabel('Año')
        plt.ylabel(self.data.columns[0])
        plt.title(f'{self.data.columns[0]} por Año')
        plt.grid(True)
        plt.show()

    def fit_model(self):
        """
        Ajusta el modelo ARIMA a los datos.
        """
        self.model = ARIMA(self.data, order=self.order)
        self.result = self.model.fit()

    def forecast(self, steps=2):
        """
        Realiza un pronóstico para un número dado de pasos hacia adelante.
        
        :param steps: Número de pasos temporales a pronosticar.
        :return: Pronóstico como un objeto de serie de Pandas.
        """
        forecast = self.result.forecast(steps=steps)
        print(forecast)
        return forecast
