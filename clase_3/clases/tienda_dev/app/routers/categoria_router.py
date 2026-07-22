from fastapi import APIRouter, HTTPException
from app.schemas.categoria_schema import CategoriaCreate
from app.services import categoria_service


router= APIRouter(prefix = '/categorias', tags= ['categorias'])

@router.post('/')
def crear (categoria: CategoriaCreate):
    nueva = categoria_service.crear_categoria(categoria)
    return{
        'mesage': 'categoria creada correctamente',
        'categoria': nueva
    }


@router.get('/')
def listar():
    resultado = categoria_service.litar_categorias()
    return {
        'total': len(resultado),
        'categorias': resultado
    }


@router.get('/{categoria_id}')
def obtener(categoria_id:int):
    categoria = categoria_service.obtener_categoria(categoria_id)
    if categoria is None:
        raise HHTPException(status_code = 404, detail = 'categoria no encontrada')
    return categoria


#actualiar y eliminar

@router.put('/')
def actualizar(categoria_id:int, datos: CategoriaCreate):
    categoria = categoria_service.actualizar_categoria(categoria_id,datos)
    if categoria is None:
        raise HHTPException(status_code = 404, detail= 'categoria no encontrada')
    return {
        'mesage': 'categoria actualizada con exito',
        'categoria': f'categoria {categoria} catualizada'
    }

@router.delete('/')
def eliminar (categoria_id:int):
    eliminada = categoria_service.eliminar_categoria(categoria_id)
    if not eliminada:
        raise HHTPException(status_code =404, detail = 'categoria no encontrada')
    return {
        'mesage': 'categoria eliminada correctamente',
        'categoria': f'categoria{categoria_id} eliminada'
    }