import sys
sys.path.append(r'C:/Users/Germán Llorente/Desktop/germiprogramer/CHAMPIONS-LEAGUE')
from classes.serie_temporal.sarima import *
from auxiliar.rutas import *

# Imaginemos que ya tenemos 'df' como DataFrame de Pandas con las columnas adecuadas
# Calcular la diferencia de goles para utilizarla en el análisis
manchester_city_liga['Gls Difference'] = manchester_city_liga['League Gls'] - manchester_city_liga['League Gls OP']

# Seleccionar las columnas 'Year' y 'Gls Difference' para el análisis
datos = manchester_city_liga[['Year', 'Gls Difference']]

# Instanciar la clase con los datos y parámetros para SARIMA
# Nota: Los parámetros (p,d,q) y (P,D,Q,s) son elegidos arbitrariamente para este ejemplo.
# Deberías ajustarlos según el análisis de tus datos.
serie_temporal = SerieTemporalSARIMA(datos, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))

# Preprocesar los datos
serie_temporal.preprocess_data()

# Visualizar los datos
serie_temporal.plot_data()

# Ajustar el modelo SARIMA
serie_temporal.fit_model()

# Pronosticar los goles de liga para los próximos 2 años
serie_temporal.forecast(steps=5)
