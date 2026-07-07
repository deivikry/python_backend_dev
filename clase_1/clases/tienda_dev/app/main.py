from fastapi import FastAPI
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

productos_bd =[]

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
    productos_bd.append(producto)
    return{
        'nombre':'produco creado exitosamente',
        'producto': producto,
    }

@app.get('/productos')
def listarProductos():
    return{
        'total': len(productos_bd),
        'nombres': productos_bd
    }