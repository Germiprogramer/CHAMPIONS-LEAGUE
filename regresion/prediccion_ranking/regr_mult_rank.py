import sys
import os 
sys.path.append('C:/Users/Germán Llorente/Desktop/germiprogramer/CHAMPIONS-LEAGUE/rutas.py')
from rutas import ch14
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd


'''
# Selecciona las variables independientes y la dependiente
X = df_total[['W_av', 'D_av', 'L_av', 'GF_av', 'GA_av', 'GD_av', 'Pts_av']]
Y = df_total['Rk_transformed']  # Asumiendo que 'Rk_transformed' es tu columna dependiente

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# Crear el modelo de regresión lineal múltiple
modelo = LinearRegression()

# Entrenar el modelo
modelo.fit(X_train, Y_train)
'''