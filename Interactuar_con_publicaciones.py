def Me_Gusta(usuario_actual, archivo_usuarios='usuarios.json', archivo_publicaciones='publicaciones.json'):
    publicaciones = leerJson(archivo_publicaciones)
    usuarios = leerJson(archivo_usuarios)
    
    ingrese = Validacion_Ingreso("INGRESE EL CODIGO DE LA PUBLICACION", 0, 1000)
    for i in publicaciones:
        if ingrese == i["numero"]:
            if usuario_actual in i["me gusta"]:
                console.print("❌ Ya has dado 'me gusta' a esta publicación.", style="bold red")
                return
            i["me gusta"].append(usuario_actual)
            console.print("👍 ¡Has dado 'me gusta' a la publicación!", style="bold green")
            escribirJson(archivo_publicaciones, publicaciones)
            return
    console.print("❌ No se encontró una publicación con ese código.", style="bold red")