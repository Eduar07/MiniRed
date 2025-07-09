# filepath: c:\Users\Usuario\OneDrive\Documentos\PROGRAMADORES\RedProgramadores\Utilidades.py
# ================================================================
# 📦 IMPORTACIONES
# ================================================================
from Utilidades import *

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