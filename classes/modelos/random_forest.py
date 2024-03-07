import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import StandardScaler

class RandomForestModel:
    def __init__(self, n_estimators=200, min_samples_split=10, min_samples_leaf=4, random_state=42):
        self.rf = RandomForestRegressor(n_estimators=n_estimators,
                                        min_samples_split=min_samples_split,
                                        min_samples_leaf=min_samples_leaf,
                                        random_state=random_state,
                                        n_jobs=-1)
        self.scaler = StandardScaler()
    
    def fit(self, X, y):
        # Escalar las características
        X_scaled = self.scaler.fit_transform(X)
        # Ajustar el modelo Random Forest
        self.rf.fit(X_scaled, y)
    
    def predict(self, X):
        # Escalar las características
        X_scaled = self.scaler.transform(X)
        # Realizar predicciones
        return self.rf.predict(X_scaled)
    
    def evaluate(self, X_test, y_test):
        # Realizar predicciones en el conjunto de prueba
        y_pred = self.predict(X_test)
        # Calcular y retornar el MAE
        return mean_absolute_error(y_test, y_pred)