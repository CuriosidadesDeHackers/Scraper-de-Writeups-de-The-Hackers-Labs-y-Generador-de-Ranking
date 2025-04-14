# 🧠 Scraper de Writeups de THL y Generador de Ranking

Este script en Python automatiza la recolección de usuarios que han resuelto retos en los laboratorios de [TheHackersLabs](https://thehackerslabs.com), genera un **ranking con puntuaciones**, y crea un **HTML visual y elegante** con los resultados.

Además, es completamente interactivo: puedes añadir nuevas URLs desde consola, y el script se autoactualiza con ellas. 🚀

---

## 🎯 ¿Qué hace este script?

- Extrae autores desde etiquetas `<kbd>` en los writeups de cada laboratorio.
- Asigna una puntuación a cada URL.
- Suma los puntos por autor.
- Genera un ranking ordenado con medallas 🥇🥈🥉 para los 3 primeros.
- Crea un archivo HTML con diseño responsivo y visual.
- Se abre automáticamente en tu navegador por defecto.
- Guarda las nuevas URLs directamente **dentro del script** (`script.py`).

---

## 📦 Requisitos

Necesitas tener **Python 3.x** instalado, además de estas librerías:

```bash
pip install requests beautifulsoup4 tqdm colorama
```
---

## 🚀 Cómo usarlo
Clona este repositorio:

```bash
Copiar
Editar
git clone https://github.com/tuusuario/thl-ranking.git
cd thl-ranking
Ejecuta el script:
```

```bash
python script.py
El script te preguntará si quieres añadir nuevas URLs. Ejemplo:
```

```bash
¿Quieres añadir nuevas URLs manualmente? Escribe 'fin' para terminar.
Introduce URL: https://thehackerslabs.com/mi-laboratorio/
Introduce puntuación (número): 4
✔ Añadido: https://thehackerslabs.com/mi-laboratorio/ con 4 puntos
Introduce URL: fin
El ranking se generará automáticamente y se abrirá en tu navegador. 🎉
```

---

## ✨ Ejemplo visual del HTML generado
El resultado se ve así en tu navegador:

![1](https://github.com/user-attachments/assets/43518761-0925-4706-a959-3bcfebe797b1)


📱 Compatible con móvil y tablet.
🎨 Fondo negro, medallas doradas, y tabla responsiva.

---

## ⚠️ Advertencia importante
🛑 Este script se modifica a sí mismo (script.py) cuando añades nuevas URLs.
✅ Si quieres mantener una versión original intacta, haz una copia antes de ejecutarlo.
🔁 Toda URL añadida se guarda dentro del propio script, en el diccionario urls.
