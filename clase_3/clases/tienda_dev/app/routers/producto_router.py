from fastapi import APIRouter, HTTPException
from app.schemas.producto_schemas import ProductoCreate
from app.services import producto_service

router = APIRouter(prefix="/productos", tags=["Productos"])

@router.post('/')
def crear (producto: ProductoCreate):
    nuevo = producto_service.crear_producto(producto)
    return { 
        'mesage': 'producto creado exitosamente', 'producto': nuevo
    }

@router.get('/')
def listar (categoria:str| None=None, precio_max: float| None=None):
    resultado = producto_service.listar_productos(categoria,precio_max)
    return {
        'total': len(resultado), 
        'productos': resultado
    }
    
@router.get('/{producto_id}')
def obtener(producto_id:int):
    producto = producto_service.obtener_producto(producto_id)
    if producto is None:
        raise HTTPException(status_code =404,detail ='producto no encontrado')
    return producto

@router.put('/{prodcuto_id}')
def actualizar(producto_id:int, datos:ProductoCreate):
    producto = producto_service.actualizar_productos(producto_id,datos)
    if producto is None:
        raise HTTPException(status_code= 404, detail = 'producto no encontrado')
    return {
        'mesage': 'producto actualizado correctamente',
        'producto': producto
    }


@router.delete('/{producto_id}')
def eliminar(producto_id:int):
    resultado= producto_service.eliminar_producto(producto_id)
    if resultado is None:
        raise HTTPException(status_code= 404, detail= 'producto no encontrado')
    return {
        'mesaje': 'producto eliminado correctamente',
        'producto': f'producto {producto_id}'
    }