from fastapi import APIRouter

router = APIRouter(prefix="/productos",
                   tags = ["Productos"],
                   responses= { 404 : {"message":"no encontrado"} } )

Productos = ["producto1", "producto2","producto3","producto4","producto5"]


@router.get("/")
#/productos
async def Listar_productos():
    return Productos

@router.get("/{id}")
#/producto/1
async def buscar_producto(id:int):
    return Productos[id]
