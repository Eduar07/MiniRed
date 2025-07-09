from questionary import prompt
from rich.console import Console
from Utilidades import *
from comentar_publicacion import *
from crearpublicaciones import *
from Inicio_de_sesion import *
from Interactuar_con_publicaciones import *
from lista_usuario import *
from navegacion import *
from publicacion import *
from registro_Usuario import *


console = Console()


def Menu_Usuario():
    console.print("=" * 80, style="bold blue")
    console.print(" BIENVENIDOS ", style="bold green")
    console.print("💻 LA RED SOCIAL CONECTA EL CÓDIGO 💻", style="bold yellow")
    
    opciones = [
        {"name": "CREAR PUBLICACION", "value": 1},
        {"name": "HISTORIAL DE PUBLICACIONES", "value": 2},
        {"name": "LISTA DE USUARIOS", "value": 3},
        {"name": "VISUALIZACION DE PUBLICACIONES", "value": 4},
        {"name": "SALIR", "value": 0},
    ]
    
    respuesta = prompt({
        'type': 'select',
        'name': 'opcion',
        'message': 'Seleccione una opción:',
        'choices': opciones,
    })
    
    return respuesta['opcion']

def Menu_Inicio():
    console.print(" BIENVENIDOS ", style="bold green")
    console.print("💻 LA RED SOCIAL CONECTA EL CÓDIGO 💻", style="bold yellow")
    
    opciones = [
        {"name": "REGISTRARSE", "value": 1},
        {"name": "INICIAR SESION", "value": 2},
    ]
    
    respuesta = prompt({
        'type': 'select',
        'name': 'opcion',
        'message': 'Seleccione una opción:',
        'choices': opciones,
    })
    
    return respuesta['opcion']

def Menu_Principal():
    console.print(" BIENVENIDOS ", style="bold green")
    console.print("💻 LA RED SOCIAL CONECTA EL CÓDIGO 💻", style="bold yellow")
    
    opciones = [
        {"name": "REGISTRARSE", "value": 1},
        {"name": "INICIAR SESION", "value": 2},
    ]
    
    respuesta = prompt({
        'type': 'select',
        'name': 'opcion',
        'message': 'Seleccione una opción:',
        'choices': opciones,
    })
    
    return respuesta['opcion']

def menuP():
    while True:
        console.print("=" * 80, style="bold magenta")
        console.print("💻 LA RED SOCIAL CONECTA EL CÓDIGO 💻", style="bold yellow")
        console.print("=" * 80, style="bold magenta")
        opcion = Menu_Principal()

        if opcion == 1:
            clear_screen()
            registrar_usuario("usuarios.json")
        elif opcion == 2:
            clear_screen()
            usuario_actual = iniciar_sesion("usuarios.json")
            while True:
                clear_screen()
                opcion_usuario = Menu_Usuario()
                if opcion_usuario == 1:
                    clear_screen()
                    crear_publicacion(usuario_actual)
                elif opcion_usuario == 2:
                    mostrar_historial(usuario_actual)
                    input("\nPresiona Enter para continuar...")
                elif opcion_usuario == 3:
                    clear_screen()
                    listar_usuarios("usuarios.json")
                    input("\nPresiona Enter para continuar...")
                elif opcion_usuario == 4:
                    while True:
                        clear_screen()
                        Ver_Publicaciones()
                        console.print("=" * 80, style="bold cyan")
                        console.print("💻 LA RED SOCIAL CONECTA EL CÓDIGO 💻", style="bold yellow")
                        console.print("=" * 80, style="bold cyan")
                        opcion_ver = prompt({
                            'type': 'select',
                            'name': 'opcion_ver',
                            'message': 'Seleccione una opción:',
                            'choices': [
                                {"name": "COMENTAR PUBLICACIONES", "value": 1},
                                {"name": "DAR LIKE A PUBLICACIONES", "value": 2},
                                {"name": "VER COMENTARIOS", "value": 3},
                                {"name": "VOLVER AL MENÚ ANTERIOR", "value": 0},
                            ],
                        })['opcion_ver']
                        if opcion_ver == 1:
                            Ver_Publicaciones()
                            Crear_Comentario(usuario_actual)
                        elif opcion_ver == 2:
                            Ver_Publicaciones()
                            Me_Gusta(usuario_actual)
                        elif opcion_ver == 3:
                            Ver_Publicaciones()
                        elif opcion_ver == 0:
                            break
                elif opcion_usuario == 0:
                    console.print("¡Hasta luego!", style="bold green")
                    break
        else:
            console.print("¡Gracias por usar la red social!", style="bold green")
            break

if __name__ == "__main__":
    menuP()
