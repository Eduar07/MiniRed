# ================================================================
# 📝 ISSUE #4 - CREAR PUBLICACIÓN
# ================================================================
from Utilidades import *
from datetime import datetime


TIPOS_PUBLICACION = {
    "1": " Noticias Tech",
    "2": " Proyectos y Código",
    "3": " Preguntas y Ayuda",
    "4": " Recursos y Aprendizaje",
    "5": " Logros y Experiencias"
}

def crear_publicacion(usuario_actual, archivo_usuarios='usuarios.json', archivo_publicaciones='publicaciones.json'):
    publicaciones_globales = leerJson(archivo_publicaciones)
    usuarios = leerJson(archivo_usuarios)

    print("\nSelecciona el tipo de publicación:")
    for clave, tipo in TIPOS_PUBLICACION.items():
        print(f"{clave}. {tipo}")

    while True:
        tipo_opcion = input("Ingrese el número del tipo de publicación: ").strip()
        if tipo_opcion in TIPOS_PUBLICACION:
            tipo_publicacion = TIPOS_PUBLICACION[tipo_opcion]
            break
        else:
            print("❌ Opción inválida. Intenta nuevamente.")

    contenido = input("\n✏️ Escribe el contenido de tu publicación:\n").strip()
    if not contenido:
        print("❌ No se puede publicar un mensaje vacío.")
        return

    nueva_publicacion = {
        "usuario": usuario_actual,
        "tipo": tipo_publicacion,
        "contenido": contenido,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    publicaciones_globales.append(nueva_publicacion)
    escribirJson(archivo_publicaciones, publicaciones_globales)

    for usuario in usuarios:
        if usuario["usuario"] == usuario_actual:
            if "publicaciones" not in usuario:
                usuario["publicaciones"] = []
            usuario["publicaciones"].append(nueva_publicacion)
            break

    escribirJson(archivo_usuarios, usuarios)
    print(f"\n✅ Publicación creada exitosamente como: {tipo_publicacion}")

# usuario_logueado = iniciar_sesion("usuarios.json")
# crear_publicacion(usuario_logueado, "usuarios.json", "publicaciones.json")