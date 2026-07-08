from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title = 'tienda dev deivi',
    descripcion = 'API BACKEN PROFESIONAL DE LA TIENDA -- DEIVI',
    version = '1.0.0'
)

class ProductoCreate(BaseModel):
    nombre: str
    precio: float
    stock: int
    categoria: str

productos_bd =[]
contador_id = 1


@app.get('/saludo')
def obtener_saludo():
    return {
        'mensaje':'hola estoy saludando  desde fastAPI desde tienda deivi',
        'estado': 'activo'
    }

@app.get('/')
def raiz():
    return{
        'menssaje':'hola bienvenido a tienda deivi',
        'version': '1.0.0'
    }

@app.get('/healt')
def healt():
    return{
        'menssaje':'200',
        'version': '1.0.0'
    }

@app.post('/crear_producto')
def crear_producto(producto: ProductoCreate):
    global contador_id
    nuevo = {
        'id': contador_id,
        'nombre': producto.nombre,
        'precio': producto.precio,
        'stock': producto.stock,
        'categoria': producto.categoria
    }
    productos_bd.append(nuevo)
    contador_id +=1
    return{
        'nombre':'produco creado exitosamente',
        'producto': producto
    }
#consultar todos
"""@app.get('/productos')
def listarProductos():
    return{
        'total': len(productos_bd),
        'nombres': productos_bd
    }
"""
#consultar por id
@app.get('/productos/{producto_id}')
def obtenerProductoId(producto_id:int):
    for p in productos_bd:
        if p['id']== producto_id:
            return p
        
    raise HTTPException(status_code=404, detail= 'producto no encontrado')

#consultar con filtros
@app.get('/productos')
def listar_productos(categoria: str |None=None, precio_max: float |None=None):
    resultado= productos_bd
    if categoria is not None:
        resultado = [p for p in resultado if p['categoria'].lower() ==categoria.lower()]
    if precio_max is not None:
        resultado = [p for p in resultado if p['precio']<= precio_max]    
    return {'total': len (resultado), 'productos': resultado}


#actualizar poducto

@app.put('/actualizar/{producto_id}')
def actualizar_producto(producto_id:int, datos:ProductoCreate):
    for p in productos_bd:
        if p['id'] == producto_id:
            p['nombre']= datos.nombre
            p['precio']= datos.precio
            p['stock']= datos.stock
            p['categoria']= datos.categoria
            return {'mensaje':'producto actualizado exitosamente', 'producto':p}
    raise HTTPException(status_code=404, detail= 'producto no encontrado')


#eliminar un producto

@app.delete('/eliminar/{producto_id}')
def eliminar_producto(producto_id: int):
    for p in productos_bd:
        if p['id']== producto_id:
            productos_bd.remove(p)
            return {'mesage:'f'producto {producto_id} elimando correctamente'}
    raise HTTPException (status_code=404, detail='producto no encontrado')
