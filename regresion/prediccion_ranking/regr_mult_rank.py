import sys
sys.path.append(r'C:/Users/Germán Llorente/Desktop/germiprogramer/CHAMPIONS-LEAGUE')
from auxiliar.functions import transform_rank
from auxiliar.rutas import *
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd

df_total = pd.concat([ch14, ch15, ch16, ch17, ch18, ch19, ch20, ch21, ch22, ch23], ignore_index=True)

# Selecciona las variables independientes y la dependiente
X = df_total[['W_av', 'L_av', 'GF_av', 'GA_av', 'GD_av', 'Pts_av']]
Y = df_total['Rk_transformed']  # Asumiendo que 'Rk_transformed' es tu columna dependiente

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# Crear el modelo de regresión lineal múltiple
modelo = LinearRegression()

# Entrenar el modelo
modelo.fit(X_train, Y_train)

# Evaluar el modelo
print(f"Coeficiente R^2 para el conjunto de entrenamiento: {modelo.score(X_train, Y_train)}")

# Predecir el 'Rk_transformed' para el conjunto de prueba

Y_pred = modelo.predict(X_test)

# Crear un DataFrame con los resultados

resultados = pd.DataFrame({'Actual': Y_test, 'Predicción': Y_pred})

print(resultados.head(10))

# Guardar el modelo entrenado

import joblib

joblib.dump(modelo, 'modelos/regresion_ranking.pkl')

# Cargar el modelo entrenado

modelo_cargado = joblib.load('modelos/regresion_ranking.pkl')

# Usar el modelo cargado para hacer predicciones

nuevos_datos = ch24[['W_av', 'L_av', 'GF_av', 'GA_av', 'GD_av', 'Pts_av']]

print(nuevos_datos.columns)

prediccion = modelo_cargado.predict(nuevos_datos)

print(prediccion)

#añaddeme esta prediccion a la tabla ch24

ch24['Rk_transformed'] = prediccion

# quiero que el menor de esos datos sea el 1, el segundo menor el 2, los dos siguientes 4, los 4 siguientes 8, los 8 siguientes 16 y todos los siguientes 32

ch24 = ch24.sort_values(by='Rk_transformed', ascending=True)

ch24['Rk_transformed'] = ch24['Rk_transformed'].rank(method='first')



def transform_rank(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    elif 3 <= x <= 4:
        return 4
    elif 5 <= x <= 8:
        return 8
    elif 9 <= x <= 16:
        return 16
    else:
        return 32
    



ch24['Rk_transformed'] = ch24['Rk_transformed'].apply(transform_rank)

ch24['Rk_transformed'] = ch24['Rk_transformed'].astype(int)

ch24 = ch24.sort_values(by='Rk_transformed', ascending=True)

print(ch24[["Squad","Rk_transformed"]])

