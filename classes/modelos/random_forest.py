import sys
sys.path.append(r'C:/Users/Germán Llorente/Desktop/germiprogramer/CHAMPIONS-LEAGUE')
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import pandas as pd
from auxiliar.rutas import *
from sklearn.preprocessing import StandardScaler




# Suponiendo que ch14, ch15, ..., ch23 ya están cargados y limpios
df_total = pd.concat([ch14, ch15, ch16, ch17, ch18, ch19, ch20, ch21, ch22, ch23], ignore_index=True)

# Definir las características y la variable objetivo
X = df_total[['W_av', 'L_av', 'GF_av', 'GA_av', 'GD_av', 'Pts_av']]
y = df_total['Rk_transformed']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Construir y ajustar el modelo de Random Forest
rf = RandomForestRegressor(n_estimators=200, random_state=42, n_jobs=-1, min_samples_split=10, min_samples_leaf=4)  # n_jobs=-1 utiliza todos los procesadores disponibles
rf.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = rf.predict(X_test)

# Evaluar el modelo
mae = mean_absolute_error(y_test, y_pred)

print(f"Error absoluto medio: {mae}")

# Preparar el nuevo conjunto de datos para la predicción
X_new = ch24[['W_av', 'L_av', 'GF_av', 'GA_av', 'GD_av', 'Pts_av']]
for col in X_new.columns:
    if X_new[col].dtype == object:
        X_new[col] = X_new[col].str.replace(',', '').astype(float)

# Realizar predicciones sobre el nuevo dataset
new_predictions = rf.predict(X_new)

# Añadir las predicciones al dataset ch24
ch24['New_Rk_transformed'] = new_predictions

# Imprimir el equipo con las nuevas predicciones
print(ch24[['Squad', 'New_Rk_transformed']])