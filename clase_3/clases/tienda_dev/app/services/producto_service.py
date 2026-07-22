productos_bd =[]
contador_id = 1




#funciones para crear  POST
def crear_producto (datos):
    global contador_id
    nuevo = {
        'id': contador_id,
        'nombre' : datos.nombre,
        'precio': datos.precio,
        'stock' : datos.stock,
        'categoria' : datos.categoria
    }
    productos_bd.append(nuevo)
    contador_id +=1
    return nuevo

#funciones para obtener GET

def listar_productos (categoria= None, precio_max=None):
    resultado = productos_bd
    if categoria is not None:
        resultado = [p for p in resultado if p['categoria'].lower()== categoria.lower]
    
    if precio_max is not None:
        resultado = [p for p in resultado if p['precio'] <= precio_max] #listar todos los productos por debajo del precio max
    return resultado


def obtener_producto (producto_id):
    for p in productos_bd:
        if p['id']== producto_id:
            return p
    

#funciones para actualizar PUT

def actualizar_productos(producto_id, datos):
    for p in productos_bd:
        if p['id']== producto_id:
            p['nombre']= datos.nombre
            p['precio']= datos.precio
            p['stock']= datos.stock
            p['categoria']= datos.categoria
            return p
    return None


#funciones para eliminar DELETE

def eliminar_producto (producto_id):
    for p in productos_bd:
        if p['id'] == producto_id:
            productos_bd.remove(p)
            return True
    return False
