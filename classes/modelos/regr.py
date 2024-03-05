import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib
import matplotlib.pyplot as plt

class Regresion:
    def __init__(self, directorio_modelo='modelos/regresion_ranking.pkl'):
        self.modelo = LinearRegression()
        self.directorio_modelo = directorio_modelo

    def entrenar(self, df_total, variables_independientes, variable_dependiente):
        X = df_total[variables_independientes]
        Y = df_total[variable_dependiente]

        # Dividir los datos
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

        # Entrenar el modelo
        self.modelo.fit(X_train, Y_train)

        # Evaluar el modelo
        print(f"Coeficiente R^2 para el conjunto de entrenamiento: {self.modelo.score(X_train, Y_train)}")

        # Predecir y mostrar resultados
        Y_pred = self.modelo.predict(X_test)
        resultados = pd.DataFrame({'Actual': Y_test, 'Predicción': Y_pred})
        print(resultados.head(10))

        # Guardar el modelo entrenado
        joblib.dump(self.modelo, self.directorio_modelo)

    def cargar_modelo(self):
        self.modelo = joblib.load(self.directorio_modelo)

    def predecir(self, nuevos_datos):
        return self.modelo.predict(nuevos_datos)


        
class RegresionRanking(Regresion):
    def __init__(self, directorio_modelo='modelos/regresion_ranking.pkl'):
        super().__init__(directorio_modelo)

    def entrenar(self, df_total, variables_independientes, variable_dependiente):
        super().entrenar(df_total, variables_independientes, variable_dependiente)
        # Aquí podrías añadir pasos adicionales específicos para la regresión de ranking.

    @staticmethod
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
        
    def ajustar_ranking(self, df, prediccion, columna_resultado='Rk_transformed'):
            df[columna_resultado] = prediccion
            df = df.sort_values(by=columna_resultado, ascending=True)
            df[columna_resultado] = df[columna_resultado].rank(method='first')
            df[columna_resultado] = df[columna_resultado].apply(self.transform_rank)
            df[columna_resultado] = df[columna_resultado].astype(int)
            return df.sort_values(by=columna_resultado, ascending=True)
    
    def visualizar_resultados(self, df):
        # Asumimos que 'df' ya tiene una columna 'Fase' con los resultados ajustados por 'ajustar_ranking'
        fase_map = {
            1: 'Ganador',
            2: 'Finalista',
            4: 'Semifinalista',
            8: 'Cuartos de Final',
            16: 'Octavos',
            32: 'Fase de Grupos'
        }

        df['Fase'] = df['Rk_transformed'].map(fase_map)


        color_map = {
            'Ganador': 'gold',
            'Finalista': 'silver',
            'Semifinalista': 'lightblue',
            'Cuartos de Final': 'lightgreen',
            'Octavos': 'wheat',
            'Fase de Grupos': 'lightgrey'
        }

        # Aplicar colores
        df['Color'] = df['Fase'].map(color_map)

        plt.figure(figsize=(8, 6))
        ax = plt.subplot(111, frame_on=False) 
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)

        cell_text = df[['Squad', 'Fase']].values
        # Asegurarse de que cell_colors tenga dos columnas, una para cada columna en cell_text
        cell_colors = [[c, c] for c in df['Color'].values]  # Duplicar el color para ambas columnas

        the_table = plt.table(cellText=cell_text,
                            colLabels=['Equipo', 'Fase'],
                            cellLoc='center',
                            cellColours=cell_colors,  # Asegúrese de que cada fila tenga 2 columnas de colores
                            loc='center')
        the_table.auto_set_font_size(False)
        the_table.set_fontsize(10)
        the_table.scale(1.2, 1.2)
        plt.show()