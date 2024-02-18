import re 
import requests
from bs4 import BeautifulSoup

website = "https://kassiesa.net/uefa/data/method5/trank10-2024.html"
resultado = requests.get(website)
content = resultado.text

soup = BeautifulSoup(content, 'html.parser')
elementos_azules = soup.find_all(class_="aleft blue")
elementos_blancos = soup.find_all(class_="aleft")
elementos_verdes = soup.find_all(class_="aleft green")
elementos_linea = soup.find_all(class_="clubline")


lista_equipos_azules = []
lista_equipos_blancos = []
lista_equipos_verdes = []

def extraer_equipos_azules(cadenas):
    # Compilamos la expresión regular para buscar el contenido entre '>'
    # y '<' después de la clase especificada
    patron = re.compile(r'<td class="aleft blue">(.+?)</td>')
    
    equipos = []
    for cadena in cadenas:
        cadena = str(cadena)
        # Buscamos todos los coincidencias en la cadena actual
        coincidencias = patron.findall(cadena)
        equipos.extend(coincidencias)
    
    return equipos

def extraer_equipos_blancos(cadenas):
    # Compilamos la expresión regular para buscar el contenido entre '>'
    # y '<' después de la clase especificada
    patron = re.compile(r'<td class="aleft">(.+?)</td>')
    
    equipos = []
    for cadena in cadenas:
        cadena = str(cadena)
        # Buscamos todos los coincidencias en la cadena actual
        coincidencias = patron.findall(cadena)
        equipos.extend(coincidencias)
    
    return equipos

def extraer_equipos_verdes(cadenas):
    # Compilamos la expresión regular para buscar el contenido entre '>'
    # y '<' después de la clase especificada
    patron = re.compile(r'<td class="aleft green">(.+?)</td>')
    
    equipos = []
    for cadena in cadenas:
        cadena = str(cadena)
        # Buscamos todos los coincidencias en la cadena actual
        coincidencias = patron.findall(cadena)
        equipos.extend(coincidencias)
    
    return equipos

equipos = extraer_equipos_azules(elementos_azules)
for equipo in equipos:
    lista_equipos_azules.append(equipo)

equipos = extraer_equipos_blancos(elementos_blancos)
for equipo in equipos:
    lista_equipos_blancos.append(equipo)

equipos = extraer_equipos_verdes(elementos_verdes)
for equipo in equipos:
    lista_equipos_verdes.append(equipo)

lista_equipos = lista_equipos_azules + lista_equipos_blancos + lista_equipos_verdes
