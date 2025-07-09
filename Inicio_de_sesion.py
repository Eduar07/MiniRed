
# ================================================================
# 🔐 ISSUE #2 - INICIO DE SESIÓN
# ================================================================
=======
from Utilidades import *
from rich.console import Console
console = Console()


console = Console()
def iniciar_sesion(path: str):
    datos = leerJson(path)
    while True:
        Usuario = Prompt.ask("Ingrese su usuario para ingresar a la cuenta:")
        espacio()
        for dato in datos:
            if dato["usuario"] == Usuario:
                while True:
                    contraseña = Verificacion_Contraseña("Ingrese su contraseña: ")
                    if dato["contrasena"] == contraseña:
                        console.print(f"Bienvenidos a nuestra red social programador {Usuario}", style="bold blue")
                        global usuario_actual
                        usuario_actual = Usuario
                        return Usuario
                    else:
                        console.print("Contraseña incorrecta", style="bold red")
                break
        else:
            console.print("Usuario no existe", style="bold red")
