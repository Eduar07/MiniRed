# ================================================================
# 🔐 ISSUE #2 - INICIO DE SESIÓN
# ================================================================
from Utilidades import *
from rich.console import Console

console = Console()
def iniciar_sesion(path: str):
    datos = leerJson(path)
    while True:
        Usuario = Validar_Texto("Ingrese su usuario para ingresar a la cuenta: ")
        espacio()
        for dato in datos:
            if dato["usuario"] == Usuario:
                while True:
                    contraseña = Verificacion_Contraseña("Ingrese su contraseña: ")
                    if dato["contrasena"] == contraseña:
                        print(f"BIENVENIDOS A NUESTRA RED SOCIAL PROGRAMADOR {Usuario}")
                        return Usuario
                    else:
                        print("Usuario no existe")
                break
        else:
            print("usuario no existe")
# Red programadores
# usuario_logueado = iniciar_sesion("usuarios.json")
