from fastapi import FastAPI, HTTPException
from app.routers import producto_router
from app.routers import categoria_router
app = FastAPI(
    title = 'tienda dev deivi',
    descripcion = 'API BACKEN PROFESIONAL DE LA TIENDA -- DEIVI',
    version = '1.0.0'
)

app.include_router(producto_router.router)
app.include_router(categoria_router.router)