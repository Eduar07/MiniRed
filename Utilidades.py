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

def Validar_Texto(mensaje: str):
    while True:
        valor = questionary.text(mensaje).ask()
        suplente = valor.replace(" ", "")
        if suplente.isalpha():
            return valor.upper()

def Verificacion_Contraseña(mensaje: str):
    while True:
        contraseña = questionary.password(mensaje).ask()
        contraseña2 = questionary.password("CONFIRMAR TU CONTRASEÑA: ").ask()
        if contraseña == contraseña2:
            console.print("CONTRASEÑA GUARDADA, EXITOSAMENTE: ", style="bold green")
            return contraseña
        else:
            console.print("VERIFICA QUE LAS CONTRASEÑAS SEAN IGUALES", style="bold red")

def Validacion_correo(mensaje: str):
    while True:
        email = questionary.text(mensaje).ask()
        if "@" not in email:
            console.print("RECUERDA QUE TU CORREO DEBE CONTENER @", style="bold red")
        elif not email.islower():
            console.print("CORREO TIENE LETRAS EN MAYUSCULA", style="bold red")
        elif any(c.isspace() for c in email):
            console.print("CORREO TIENE ESPACIOS", style="bold red")
        else:
            console.print("CORREO INGRESADO CORRECTAMENTE", style="bold green")
            return email

def Validacion_Telefono(mensaje: str):
    while True:
        try:
            telefono = int(questionary.text(mensaje).ask())
            lista = [int(d) for d in str(telefono)]
            if lista[0] != 3:
                console.print("RECUERDA QUE SU NUMERO DEBE INICIAR EN 3", style="bold red")
            elif len(lista) != 10:
                console.print("RECUERDA QUE SU NUMERO DEBE CONTENER 10 DIGITOS", style="bold red")
            else:
                console.print("TU NUMERO HA SIDO INGRESADO", style="bold green")
                return telefono
        except ValueError:
            console.print("INGRESE SOLO NUMEROS", style="bold red")

def Validacion_Ingreso(mensaje: str, valorminimo: int = 0, valormaximo: int = 6):
    while True:
        try:
            valor = int(questionary.text(mensaje).ask())
            if valorminimo <= valor <= valormaximo:
                return valor
            else:
                console.print(f"POR FAVOR INGRESE VALORES ENTRE {valorminimo} y {valormaximo}.", style="bold red")
        except ValueError:
            console.print("ENTRADA NO VALIDA POR FAVOR INGRESE NUMEROS", style="bold red")

def numero_aleatorio():
    return random.randint(1, 1000)