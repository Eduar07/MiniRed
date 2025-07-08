from Utilidades import *
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from datetime import datetime



global usuario_actual

console = Console()

def registro_usuario(nombre: str, telefono: int, correo: str, cedula: int, contrasena: str, usuario: str):
    return {
        "cedula": cedula,
        "nombre": nombre,
        "telefono": telefono,
        "correo": correo,
        "contrasena": contrasena,
        "usuario": usuario,
        "publicaciones": []
    }

def registrar_usuario(archivo_json: str):
    usuarios_existentes = leerJson(archivo_json)
    
    nombre = Prompt.ask("Ingrese el nombre del usuario:")
    telefono = Validacion_Telefono(f"Ingrese el número de teléfono de {nombre}: ")
    cedula = Validacion_Ingreso(f"Por favor registrar su cédula {nombre}: ", 1000000, 9999999999)
    correo = Validacion_correo(f"Por favor digitar su correo electrónico {nombre}: ")
    usuario = Prompt.ask(f"Ingrese el usuario para {nombre}:")
    contrasena = Verificacion_Contraseña(f"Ingrese la contraseña para {nombre}: ")
    
    nuevo_registro = registro_usuario(nombre, telefono, correo, cedula, contrasena, usuario)
    usuarios_existentes.append(nuevo_registro)
    escribirJson(archivo_json, usuarios_existentes)
    
    console.print("Usuario registrado con éxito", style="bold green")