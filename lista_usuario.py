# ================================================================
# 📃 ISSUE #3 - LISTAR USUARIOS
# ================================================================

def listar_usuarios(datos: str):
    usuarios = leerJson(datos)

    if not usuarios:
        print("No hay usuarios registrados.")
        return
    
    print("=" * 80)
    print("🌟 LISTA DE PROGRAMADORES REGISTRADOS EN LA RED SOCIAL 🌟".center(80))
    print("=" * 80)
    print()

    for index, usuario in enumerate(usuarios, start=1):
        print(f"👤 USUARIO #{index}")
        print(f"   📝 Nombre:     {usuario['nombre']}")
        print(f"   📞 Teléfono:   {usuario['telefono']}")
        print(f"   🆔 Cédula:     {usuario['cedula']}")
        print(f"   📧 Correo:     {usuario['correo']}")
        print(f"   👨‍💻 Usuario:    {usuario['usuario']}")
        print("-" * 50)
    
    print()
    print("=" * 80)
    print("💻 LA RED SOCIAL CONECTA EL CÓDIGO 💻".center(80))
    print("=" * 80)

# listar_usuarios("usuarios.json")
