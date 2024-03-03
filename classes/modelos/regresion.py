import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

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
