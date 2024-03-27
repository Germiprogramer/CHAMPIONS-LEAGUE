import sys
sys.path.append(r'C:/Users/Germán Llorente/Desktop/germiprogramer/CHAMPIONS-LEAGUE')
from auxiliar.rutas import *
from classes.modelos.decision_tree import *

df_total = pd.concat([ch15, ch16, ch17, ch18, ch19, ch20, ch21, ch22, ch23], ignore_index=True)

# Instanciar la clase RegresionRanking
regresion_ranking = DecisionTreeRanking('datos/modelos/decisiontree.pkl')

# Entrenar el modelo con los datos cargados
variables_independientes = ['W_av', 'L_av', 'GF_av', 'GA_av', 'GD_av', 'Pts_av', 'UEFA points']
variable_dependiente = 'Rk_transformed'
regresion_ranking.entrenar(df_total, variables_independientes, variable_dependiente)

# Cargar nuevos datos para hacer predicciones
nuevos_datos = ch24[variables_independientes]

# Usar el método predecir de la clase para obtener las predicciones
prediccion = regresion_ranking.predecir(nuevos_datos)

# Añadir la predicción a la tabla ch24
ch24['Rk_transformed'] = prediccion

# Ajustar el ranking utilizando el método ajustar_ranking de la clase
prediccion = regresion_ranking.ajustar_ranking(ch24, prediccion)

# Mostrar los resultados
prediccion = prediccion[["Squad", "Rk_transformed"]]

#guardame el dataset prediccion en un csv

prediccion.to_csv(r"C:\Users\Germán Llorente\Desktop\germiprogramer\CHAMPIONS-LEAGUE\datos\predicciones\clasif_ch_decisiontree_UEFA_points.csv", index=False)

# Mostrar los resultados

regresion_ranking.visualizar_resultados(prediccion)