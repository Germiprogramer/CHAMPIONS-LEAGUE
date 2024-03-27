import sys
sys.path.append(r'C:/Users/Germán Llorente/Desktop/germiprogramer/CHAMPIONS-LEAGUE')
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import joblib
import matplotlib.pyplot as plt
from auxiliar.rutas import *

class DecisionTree():
    def __init__(self, directorio_modelo='modelos/arbol_decision_ranking.pkl'):
        self.modelo = DecisionTreeRegressor()
        self.directorio_modelo = directorio_modelo

    def entrenar(self, df_total, variables_independientes, variable_dependiente):
        X = df_total[variables_independientes]
        Y = df_total[variable_dependiente]

        # Dividir los datos
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

        # Entrenar el modelo
        self.modelo.fit(X_train, Y_train)

        # Evaluar el modelo
        print(f"Puntuación R^2 para el conjunto de entrenamiento: {self.modelo.score(X_train, Y_train)}")

        # Predecir y mostrar resultados
        Y_pred = self.modelo.predict(X_test)
        resultados = pd.DataFrame({'Actual': Y_test, 'Predicción': Y_pred})

        # Guardar el modelo entrenado
        joblib.dump(self.modelo, self.directorio_modelo)

    def cargar_modelo(self):
        self.modelo = joblib.load(self.directorio_modelo)

    def predecir(self, nuevos_datos):
        return self.modelo.predict(nuevos_datos)

class DecisionTreeRanking(DecisionTree):
    def __init__(self, directorio_modelo='modelos/arbol_decision_ranking.pkl'):
        super().__init__(directorio_modelo)

    def entrenar(self, df_total, variables_independientes, variable_dependiente):
        super().entrenar(df_total, variables_independientes, variable_dependiente)
        # Aquí podrías añadir pasos adicionales específicos para la regresión de ranking usando árbol de decisión.

    def ajustar_ranking(self, df, prediccion, columna_resultado='Rk_transformed'):
            df[columna_resultado] = prediccion
            df = df.sort_values(by=columna_resultado, ascending=True)
            df[columna_resultado] = df[columna_resultado].rank(method='first')
            return df.sort_values(by=columna_resultado, ascending=True)
    
    
       # Definiendo una función para asignar colores basada en más grupos de clasificación
    def assign_colors(self, rank, total_ranks):
        if rank <= total_ranks / 6:
            return "#66ff66"  # Verde más claro
        elif rank <= total_ranks / 3:
            return "#99ff99"  # Verde
        elif rank <= total_ranks / 2:
            return "#ffff99"  # Amarillo
        elif rank <= 2 * total_ranks / 3:
            return "#ffcc99"  # Naranja
        elif rank <= 5 * total_ranks / 6:
            return "#ff9999"  # Rojo claro
        else:
            return "#ff6666"  # Rojo oscuro
    def visualizar_resultados(self, df):
        # Aplicando la función para definir los colores de las celdas
        total_ranks = len(df)
        cell_colors = [[self.assign_colors(rank, total_ranks) for _ in range(2)] for rank in df["Rk_transformed"]]

        plt.figure(figsize=(10, 8))
        ax = plt.subplot(111, frame_on=False)  # no visible frame
        ax.xaxis.set_visible(False)  # hide the x axis
        ax.yaxis.set_visible(False)  # hide the y axis

        table = plt.table(cellText=df.values, colLabels=df.columns, loc='center', cellLoc='center', cellColours=cell_colors)
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.scale(1.2, 1.2)

        plt.savefig("resultados/graficos/clasificacion_decisiontree_UEFApoints", bbox_inches='tight')
        plt.show()

 