# filepath: c:\Users\Usuario\OneDrive\Documentos\PROGRAMADORES\RedProgramadores\Utilidades.py
# ================================================================
# 📦 IMPORTACIONES
# ================================================================
import os
import random
import json
from datetime import datetime
import questionary
from rich.console import Console
from rich.text import Text
from rich.prompt import Prompt
from rich.table import Table
from datetime import datetime


console = Console()

# ================================================================
# 📁 FUNCIONES PARA MANEJO DE ARCHIVOS JSON (ISSUE GLOBAL)
# ================================================================

def leerJson(path: str):
    try:
        with open(path, mode='r') as file:
            datos = json.load(file)
            return datos
    except FileNotFoundError:
        return []

def escribirJson(path: str, data: list):
    with open(path, mode='w') as file:
        json.dump(data, file, indent=4)

# ================================================================
# 🛠️ FUNCIONES DE UTILIDAD (ISSUE GLOBAL)
# ================================================================

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def espacio():
    console.print("\n" * 1)

def Ver_Publicaciones(archivo_Publicaciones="publicaciones.json"):
    clear_screen()
    datos = leerJson(archivo_Publicaciones)
    if not datos:
        console.print("No hay publicaciones aún.", style="bold yellow")
        return
    table = Table(title="📰 PUBLICACIONES DE LA RED", show_lines=True)
    table.add_column("ID", style="cyan", justify="center")
    table.add_column("Usuario", style="magenta")
    table.add_column("Tipo", style="green")
    table.add_column("Contenido", style="yellow")
    table.add_column("Fecha", style="white")
    table.add_column("Likes", style="red", justify="center")
    for pub in datos:
        table.add_row(
            str(pub['numero']),
            pub['usuario'],
            pub['tipo'],
            pub['contenido'],
            pub['fecha'],
            str(len(pub.get("me gusta", [])))
        )
    console.print(table)