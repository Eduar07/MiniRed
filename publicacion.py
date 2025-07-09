# filepath: c:\Users\Usuario\OneDrive\Documentos\PROGRAMADORES\RedProgramadores\Utilidades.py
# ================================================================
# 📦 IMPORTACIONES
# ================================================================
from Utilidades import *
from rich.console import Console
from rich.table import Table

console = Console()
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

def mostrar_historial(usuario_actual, archivo_Publicaciones="publicaciones.json"):
    from questionary import prompt
    clear_screen()
    datos = leerJson(archivo_Publicaciones)
    publicaciones_usuario = [p for p in datos if p["usuario"] == usuario_actual]
    if not publicaciones_usuario:
        console.print("No tienes publicaciones aún.", style="bold yellow")
        return

    table = Table(title=f"📝 HISTORIAL DE PUBLICACIONES DE {usuario_actual}", show_lines=True)
    table.add_column("ID", style="cyan", justify="center")
    table.add_column("Tipo", style="green")
    table.add_column("Contenido", style="yellow")
    table.add_column("Fecha", style="white")
    table.add_column("Likes", style="red", justify="center")
    table.add_column("Comentarios", style="blue", justify="center")
    for pub in publicaciones_usuario:
        table.add_row(
            str(pub['numero']),
            pub['tipo'],
            pub['contenido'],
            pub['fecha'],
            str(len(pub.get("me gusta", []))),
            str(len(pub.get("comentario", [])))
        )
    console.print(table)

    # Opción para ver detalles de una publicación
    ids = [str(pub['numero']) for pub in publicaciones_usuario]
    ids.append("Salir")
    opcion = prompt({
        'type': 'select',
        'name': 'pub_id',
        'message': '¿Deseas ver los comentarios y me gusta de alguna publicación?',
        'choices': ids
    })['pub_id']

    if opcion != "Salir":
        seleccionada = next((p for p in publicaciones_usuario if str(p["numero"]) == opcion), None)
        if seleccionada:
            # Mostrar comentarios
            comentarios = seleccionada.get("comentario", [])
            if comentarios:
                console.print(f"\n[bold blue]Comentarios de la publicación {opcion}:[/bold blue]")
                for c in comentarios:
                    console.print(
                        f"[green]{c['usuario']}[/green] "
                        f"[white]({c['fecha']}):[/white] "
                        f"[yellow]{c['comentario']}[/yellow]"
                    )
            else:
                console.print("Esta publicación no tiene comentarios.", style="bold yellow")
            # Mostrar me gusta
            me_gusta = seleccionada.get("me gusta", [])
            if me_gusta:
                console.print(f"\n[bold red]Me gusta la publicación {opcion}:[/bold red]")
                for usuario in me_gusta:
                    console.print(f"[magenta]❤ {usuario}[/magenta]")
            else:
                console.print("Esta publicación no tiene reacciones de me gusta.", style="bold yellow")

