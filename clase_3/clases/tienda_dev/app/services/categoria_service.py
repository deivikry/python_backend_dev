categoria_db = []
contador_id = 1


#crear categorias

def  crear_categoria(datos):
    global contador_id
    nueva = {
        'id': contador_id,
        'nombre': datos.nombre
    }
    categoria_db.append(nueva)
    contador_id+=1
    return nueva

#listar y obtener categorias por id

def litar_categorias():
    return categoria_db


def obtener_categoria(categoria_id):
    for c in categoria_db:
        if c['id']==categoria_id:
            return c
    return None


#actualizar y eliminar

def actualizar_categoria(categoria_id, datos):
    for c in categoria_db:
        if c['id']==categoria_id:
            c['nombre']= datos.nombre
            return c
    return None

def eliminar_categoria(categoria_id):
    for c in categoria_db:
        if c['id']==categoria_id:
            categoria_db.remove(c)
            return True
    return False