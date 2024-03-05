# Crearemos el gráfico que incluya una tabla con cada equipo y su correspondiente fase alcanzada en la competición.
import sys
sys.path.append(r'C:/Users/Germán Llorente/Desktop/germiprogramer/CHAMPIONS-LEAGUE')
from classes.modelos.regr import * 
from auxiliar.rutas import *
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datos/predicciones/clasif_ch_regresion.csv")
fase_map = {
    1: 'Ganador',
    2: 'Finalista',
    4: 'Semifinalista',
    8: 'Cuartos de Final',
    16: 'Octavos',
    32: 'Fase de Grupos'
}

df['Fase'] = df['Rk_transformed'].map(fase_map)

# Ordenar el DataFrame por la fase de la competición
df_sorted = df.sort_values(by='Rk_transformed')

# Mapeamos las fases a colores
color_map = {
    'Ganador': 'gold',
    'Finalista': 'silver',
    'Semifinalista': 'lightblue',
    'Cuartos de Final': 'lightgreen',
    'Octavos': 'wheat',
    'Fase de Grupos': 'lightgrey'
}

# Obtenemos los colores para cada fila basándonos en la columna 'Fase'
row_colors = df_sorted['Fase'].map(color_map)

# Crear la figura para la tabla
plt.figure(figsize=(8, 6))
ax = plt.subplot(111, frame_on=False)  # no visible frame
ax.xaxis.set_visible(False)  # hide the x axis
ax.yaxis.set_visible(False)  # hide the y axis

# Preparar los datos de la tabla eliminando la columna 'Rk_transformed'
df_for_table = df_sorted.drop('Rk_transformed', axis=1)
cell_text = df_for_table.values

# Preparar los colores de las celdas para la columna 'Fase'
cell_colors = [[row_colors.iloc[i] if j == 1 else 'w' for j in range(len(df_for_table.columns))] for i in range(len(df_for_table))]

# Crear y mostrar la tabla
the_table = plt.table(cellText=cell_text,
                      colLabels=df_for_table.columns,
                      colWidths=[0.4, 0.4],
                      cellLoc='center',
                      cellColours=cell_colors,
                      loc='center')

the_table.auto_set_font_size(False)
the_table.set_fontsize(10)
the_table.scale(1.2, 1.2)

plt.show()