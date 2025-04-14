import requests
from bs4 import BeautifulSoup
from collections import defaultdict
from tqdm import tqdm
from colorama import Fore, Style, init
import webbrowser
import os

init(autoreset=True)

# === Diccionario de URLs con puntuaciones
urls = {
    "https.//thehackerslabs.com": 6,
    "https.//thehackerslabs.com": 5,
}

# === Pedir nuevas URLs
def pedir_urls_extra():
    print(f"{Fore.CYAN}¿Quieres añadir nuevas URLs manualmente? Escribe 'fin' para terminar.")
    nuevas_urls = {}
    while True:
        url = input(f"{Fore.YELLOW}Introduce URL: ").strip()
        if url.lower() == "fin":
            break
        try:
            puntos = int(input("Introduce puntuación (número): "))
            nuevas_urls[url] = puntos
            print(f"{Fore.GREEN}✔ Añadido: {url} con {puntos} puntos\n")
        except ValueError:
            print(f"{Fore.RED}❌ Puntuación no válida. Intenta de nuevo.\n")
    return nuevas_urls

# === Scrapeador de nombres
def obtener_nombres_writeups(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            bloques = soup.find_all('div', class_='wp-block-kenta-blocks-paragraph')
            nombres = []
            for bloque in bloques:
                nombres.extend([kbd.get_text(strip=True) for kbd in bloque.find_all('kbd')])
            return nombres
    except:
        pass
    return []

# === Calcular puntuaciones
def calcular_puntuaciones(urls):
    puntuaciones = defaultdict(int)
    for url, valor in tqdm(urls.items(), desc=f"{Fore.MAGENTA}Procesando"):
        nombres = obtener_nombres_writeups(url)
        for nombre in nombres:
            nombre = nombre.strip().lower()
            if nombre:
                puntuaciones[nombre] += valor
    return sorted(puntuaciones.items(), key=lambda x: x[1], reverse=True)

# === Generar HTML
def generar_html(puntuaciones):
    html = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ranking De Creadores</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: black;
            color: white;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            table-layout: fixed;
        }
        th, td {
            border: 1px solid #ff6900;
            padding: 8px;
            text-align: center;
            word-wrap: break-word;
        }
        th {
            background-color: #ff6900;
            color: #000000;
        }
        tr:nth-child(even) {
            background-color: black;
        }
        tr:nth-child(odd) {
            background-color: black;
        }
        @media (max-width: 768px) {
            th, td {
                font-size: 12px;
                padding: 4px;
            }
            table {
                font-size: 12px;
            }
        }
    </style>
</head>
<body>
    <table>
        <thead>
            <tr>
                <th>POSICIÓN</th>
                <th>USUARIO</th>
                <th>PUNTUACIÓN</th>
            </tr>
        </thead>
        <tbody>
"""
    for idx, (nombre, puntuacion) in enumerate(puntuaciones, start=1):
        if idx == 1:
            nombre = f"🥇{nombre}"
        elif idx == 2:
            nombre = f"🥈{nombre}"
        elif idx == 3:
            nombre = f"🥉{nombre}"
        html += f"""
            <tr>
                <td>{idx}</td>
                <td>{nombre}</td>
                <td>{puntuacion}</td>
            </tr>
        """
    html += """
        </tbody>
    </table>
</body>
</html>
"""
    return html

# === Reescribir el propio script con las nuevas URLs
def actualizar_script_con_urls(nuevas_urls):
    archivo_script = os.path.abspath(__file__)
    with open(archivo_script, "r", encoding="utf-8") as f:
        contenido = f.read()

    inicio = contenido.find("urls = {")
    fin = contenido.find("}", inicio) + 1
    nuevo_diccionario = "urls = {\n"
    for url, valor in sorted(nuevas_urls.items()):
        nuevo_diccionario += f'    "{url}": {valor},\n'
    nuevo_diccionario += "}"

    contenido_actualizado = contenido[:inicio] + nuevo_diccionario + contenido[fin:]
    with open(archivo_script, "w", encoding="utf-8") as f:
        f.write(contenido_actualizado)
    print(f"{Fore.BLUE}🔁 Script actualizado con las nuevas URLs.\n")

# === MAIN
if __name__ == '__main__':
    nuevas = pedir_urls_extra()
    if nuevas:
        urls.update(nuevas)
        actualizar_script_con_urls(urls)

    puntuaciones = calcular_puntuaciones(urls)
    html_resultado = generar_html(puntuaciones)

    with open("ranking.html", "w", encoding="utf-8") as file:
        file.write(html_resultado)

    print(f"\n{Fore.GREEN}✅ HTML generado correctamente en 'ranking.html' 🎉")
    webbrowser.open("ranking.html")
