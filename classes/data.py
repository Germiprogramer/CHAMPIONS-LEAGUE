import os
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

ruta_2019 = r"C:\Users\Germán Llorente\Desktop\germiprogramer\CHAMPIONS-LEAGUE\datos\datos_limpios\champions2019_limp.csv"

class SoccerDataAnalysis:
    def __init__(self, filepath):
        """
        Inicializa la clase cargando los datos desde un archivo CSV.
        """
        self.df = pd.read_csv(filepath)
        self.model = None

    def preprocess_data(self):
        """
        Preprocesa los datos para la regresión, convirtiendo columnas no numéricas y tratando valores faltantes si es necesario.
        """
        # Convertir 'Attendance' a numérico, eliminando comas y manejando valores faltantes
        self.df['Attendance'] = pd.to_numeric(self.df['Attendance'].str.replace(',', ''), errors='coerce')

        # Rellenar valores faltantes en 'Attendance' con la media, si se desea
        self.df['Attendance'].fillna(self.df['Attendance'].mean(), inplace=True)

        # Asegúrate de tratar otros valores faltantes o realizar más preprocesamiento según sea necesario

    def perform_multilinear_regression(self, target='Rk_transformed'):
        """
        Realiza una regresión lineal múltiple con 'target' como variable dependiente.
        """
        # Definir las variables independientes (X) y la dependiente (Y)
        X = self.df.drop(columns=[target, 'Rk', 'Squad', 'team_id'])  # Excluir columnas no numéricas y el target
        Y = self.df[target]

        # Dividir los datos en conjuntos de entrenamiento y prueba
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

        # Crear y entrenar el modelo
        self.model = LinearRegression()
        self.model.fit(X_train, Y_train)

        # Opcional: imprimir el rendimiento del modelo
        print(f"Modelo entrenado. Coeficiente R^2 para el conjunto de prueba: {self.model.score(X_test, Y_test)}")

    def predict_rank(self, new_data):
        """
        Predice el 'Rk_transformed' para nuevos datasets que no tienen definido el 'Rk'.
        """
        if self.model is None:
            print("Primero debe entrenar el modelo.")
            return None

        # Asegurarse de que new_data es un DataFrame y tiene las columnas correctas
        prediction = self.model.predict(new_data)
        return prediction

# Uso de la clase
# filepath = 'tu_archivo.csv'
# analysis = SoccerDataAnalysis(filepath)
# analysis.preprocess_data()
# analysis.perform_multilinear_regression()
# new_data = pd.DataFrame(...)  # Asegúrate de que este DataFrame tenga el mismo esquema que el utilizado para entrenar, excluyendo 'Rk'
# predictions = analysis.predict_rank(new_data)
# print(predictions)
    
ch16 = SoccerDataAnalysis(ruta_2019)
ch16.preprocess_data()
ch16.perform_multilinear_regression()
#poner los datos de la nueva temporada
new_data = 
predictions = ch16.predict_rank(new_data)
print(predictions)