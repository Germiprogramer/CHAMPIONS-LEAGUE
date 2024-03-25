# Asumiendo que 'df' ya está definido con tus datos
import sys
sys.path.append(r'C:/Users/Germán Llorente/Desktop/germiprogramer/CHAMPIONS-LEAGUE')
from classes.serie_temporal.arima import *
from auxiliar.rutas import *
# Instanciar la clase
manchester_city_liga['Gls Difference'] = manchester_city_liga['League Gls'] - manchester_city_liga['League Gls OP']

datos = manchester_city_liga[['Year', 'Gls Difference']]

serie_temporal = SerieTemporalARIMA(datos)

# Preprocesar los datos
serie_temporal.preprocess_data()

# Visualizar los datos
serie_temporal.plot_data()

# Ajustar el modelo ARIMA
serie_temporal.fit_model()

# Pronosticar los goles de liga para los próximos 2 años
serie_temporal.forecast(steps=2)