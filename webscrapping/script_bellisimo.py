import re 
from colorama import Fore
import requests
from bs4 import BeautifulSoup

website = "https://www.footballseeding.com/uefa/club-ranking/2023-24/"
resultado = requests.get(website)
content = resultado.text

soup = BeautifulSoup(content, 'html.parser')
print(soup.prettify())
elementos = soup.find_all(class_="stickyColumn")

for elemento in elementos:
    print(elemento)

'''
patron = r"/stickyColumn/[\w-]*"
maquinas_repetidas = re.findall(patron, str(content))
print(maquinas_repetidas)
sin_duplicados = list(set(maquinas_repetidas))

maquinas_final = []

for i in sin_duplicados:
    nombre_maquinas = i.replace("/entry/", "")
    maquinas_final.append(nombre_maquinas)
    print(nombre_maquinas)
'''