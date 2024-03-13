import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import joblib
import matplotlib.pyplot as plt

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
        print(resultados.head(10))

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

    # Los métodos transform_rank, ajustar_ranking y visualizar_resultados permanecen iguales
    # ya que estos métodos no dependen del tipo de modelo de regresión utilizado.