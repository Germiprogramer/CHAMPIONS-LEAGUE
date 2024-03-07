import sys
sys.path.append(r'C:/Users/Germán Llorente/Desktop/germiprogramer/CHAMPIONS-LEAGUE')
from auxiliar.rutas import *
from classes.modelos.random_forest import *

# Suponiendo que tus DataFrames ya están cargados y limpios
df_total = pd.concat([ch14, ch15, ch16, ch17, ch18, ch19, ch20, ch21, ch22, ch23], ignore_index=True)
    
X = df_total[['W_av', 'L_av', 'GF_av', 'GA_av', 'GD_av', 'Pts_av']]
y = df_total['Rk_transformed']
    
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
# Instanciar y utilizar la clase RandomForestModel
model = RandomForestModel()
model.fit(X_train, y_train)
mae = model.evaluate(X_test, y_test)
    
print(f"Error absoluto medio: {mae}")
    
# Preparar y realizar predicciones sobre un nuevo conjunto de datos
X_new = ch24[['W_av', 'L_av', 'GF_av', 'GA_av', 'GD_av', 'Pts_av']]
for col in X_new.columns:
    if X_new[col].dtype == object:
        X_new[col] = X_new[col].str.replace(',', '').astype(float)

ch24['New_Rk_transformed'] = model.predict(X_new)
    
print(ch24[['Squad', 'New_Rk_transformed']])