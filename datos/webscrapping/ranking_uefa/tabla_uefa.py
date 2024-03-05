import re 
import requests
from bs4 import BeautifulSoup
import pandas as pd

website = "https://kassiesa.net/uefa/data/method5/trank10-2024.html"
resultado = requests.get(website)
content = resultado.text

soup = BeautifulSoup(content, 'html.parser')

elementos_linea = soup.find_all("tr", class_="clubline")

data = []
for row in elementos_linea:
    cols = row.find_all(['td', 'th'])  # Busca tanto td como th para incluir la columna de suma total
    cols = [ele.text.strip() for ele in cols]
    # Asume que el primer elemento td (índice de equipo) está presente, omite la imagen
    data.append([cols[0]] + cols[2:])  # Omite la columna de imagen/estado

# Crea un DataFrame con los datos
# Define los nombres de las columnas según corresponda; aquí solo pongo algunos ejemplos genéricos
column_names = ['Rank', 'Team', 'Country', '14/15', '15/16', '16/17', '17/18', '18/19', '19/20', '20/21', '21/22', '22/23', '23/24', 'Title points', 'Total points', 'Country part']
df = pd.DataFrame(data, columns=column_names)

print(df.head(3))
df.to_csv('ranking_UEFA.csv', index=False)
