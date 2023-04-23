from fastapi import APIRouter

router = APIRouter()

Productos = ["producto1", "producto2","producto3","producto4","producto5"]


@router.get("/productos")
#/productos
async def Listar_productos():
    return Productos

@router.get("/producto/{id}")
#/producto/1
async def buscar_producto(id:int):
    return Productos[id]
