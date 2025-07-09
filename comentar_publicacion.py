def Crear_Comentario(usuario_actual, archivo_usuarios='usuarios.json', archivo_publicaciones='publicaciones.json'):
    publicaciones = leerJson(archivo_publicaciones)
    usuarios = leerJson(archivo_usuarios)
    
    ingrese = Validacion_Ingreso("INGRESE EL CODIGO DE LA PUBLICACION", 0, 1000)
    for i in publicaciones:
        if ingrese == i["numero"]:
            comentario = Prompt.ask("INGRESE EL COMENTARIO:")
            if not comentario:
                console.print("❌ No se puede publicar un mensaje vacío.", style="bold red")
                return
            Nuevo_Comentario = {
                "usuario": usuario_actual,
                "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "comentario": comentario
            }
            i["comentario"].append(Nuevo_Comentario)
            
    escribirJson(archivo_publicaciones, publicaciones)
  
#comentario sobre redprogramadores.