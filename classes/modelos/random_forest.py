import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

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
    
class RandomForestRanking(RandomForestModel):
    def __init__(self, n_estimators=200, min_samples_split=10, min_samples_leaf=4, random_state=42):
        super().__init__(n_estimators, min_samples_split, min_samples_leaf, random_state)


        
    def visualizar_resultados(self, df):
        df = df.sort_values('Rk_transformed', ascending=False)
    
        # Generar una lista de colores basada en los valores de 'Rk_transformed'
        colors = df['Rk_transformed'].apply(lambda x: 'gold' if x <= 3 else
                                            ('silver' if x <= 8 else 
                                            ('orange' if x <= 16 else 'red')))
        
        # Crear el gráfico
        plt.figure(figsize=(10, 8))
        bars = plt.barh(df['Squad'], df['Rk_transformed'], color=colors)
        plt.xlabel('Puntaje ranking predicho')
        plt.ylabel('Equipos')
        plt.title('Predicciones del ranking para cada equipo')
        
        # Crear la leyenda
        legend_elements = [Patch(facecolor='gold', label='Equipos Top'),
                        Patch(facecolor='silver', label='Grandes Equipos'),
                        Patch(facecolor='orange', label='Buenos Equipos'),
                        Patch(facecolor='red', label='Equipos Mediocres')]
        plt.legend(handles=legend_elements, title='Niveles del ranking')
        
        # Invertir el orden del eje y para que el mejor ranking esté arriba
        plt.gca().invert_yaxis()
        
        # Mostrar el gráfico
        plt.tight_layout()
        plt.savefig("resultados/graficos/clasificacion_random_forest", bbox_inches='tight')
        plt.close()  # Cerrar la figura para evitar que se muestre en otro output
            
            