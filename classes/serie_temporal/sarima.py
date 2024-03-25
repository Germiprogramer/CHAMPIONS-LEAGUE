import pandas as pd
import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAX
import matplotlib.pyplot as plt

class SerieTemporalSARIMA:
    def __init__(self, data, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12)):
        """
        Inicializa la instancia de la clase con los datos, el orden del modelo SARIMA y el orden estacional.
        
        :param data: DataFrame de Pandas con dos columnas: 'Year' y la variable de interés.
        :param order: Una tupla (p, d, q) que representa el orden del modelo no estacional.
        :param seasonal_order: Una tupla (P, D, Q, s) que representa el orden estacional del modelo SARIMA.
        """
        self.data = data
        self.order = order
        self.seasonal_order = seasonal_order
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
        Ajusta el modelo SARIMA a los datos.
        """
        self.model = SARIMAX(self.data, order=self.order, seasonal_order=self.seasonal_order)
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