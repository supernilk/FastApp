from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/usuario",
                   tags = ["usuario"],
                   responses= { 404 : {"message":"no encontrado"} } )

#-----------------  Iniciar el server  -----------------  
#pyenv local 3.7.4
#python -m venv venv
#.\venv\Scripts\activate
#py -m uvicorn user:app --reload

#pip freeze     <--- ver la lista de paquetes instalados
#pip install "fastapi[all]"
#pip install "uvicorn[standard]"

#py -m pip install --upgrade pi

#https://www.youtube.com/watch?v=dAQENEPAqsc&t=99s

#Entidad usuario
class Usuario(BaseModel):
    id: int
    nombre: str
    apellido: str
    url: str
    edad: int

#lista que puede provenir de una base de datos
#user_list
Usuarios = [Usuario(id=1, nombre="John", apellido="Barragan", url="html://google.co.ve",edad=45),
            Usuario(id=2, nombre="Pedro", apellido="Perez", url="html://perez.com",edad=23),
            Usuario(id=3, nombre="ana", apellido="rodriguez", url="html://zorras.us",edad=18)]

@router.get("/")
#/usuarios
async def listar_usuarios():
    return Usuarios


@router.get("/{ide}")# Path
#/usuario/1
async def buscar_usuario(ide:int):
    return buscar_usuario(ide)


@router.get("/")# Query
#/usuario/?id=1
async def buscar_usuario(id:int):
    return buscar_usuario(id)

@router.post("/", response_model = Usuario, status_code = 201)#creamos un nuevo usuario
async def crear_usuario(usuario:Usuario):
#    return "agregando usuario con Usuario"
    if type( buscar_usuario(usuario.id) ) == Usuario:
        raise HTTPException(status_code=404)
        #return {"error":"usuario ya existe"}
    else: 
        Usuarios.append(usuario)
        return usuario
            
@router.put("/")#actualizar un nuevo usuario
async def actualizar_usuario(usuario:Usuario):
    encontrado=False
    for index, consultar_usuario in enumerate(Usuarios):
        if consultar_usuario.id==usuario.id:
            Usuarios[index]=usuario
            encontrado=True
    
    if not encontrado:
        return {"error":"no se ha actualizado el usuario"}
    else:
        return usuario

@router.delete("/{id}")# borramos un usuario
#/usuario/1
async def borra_usuario(id:int):
    encontrado=False
    for index, consultar_usuario in enumerate(Usuarios):
        if consultar_usuario.id==id:
            del Usuarios[index]
            encontrado=True

    if not encontrado:
        return {"error":"no se ha borrado el usuario"}
    else:
        return {"usuario borrado"}
    


def buscar_usuario(id:int):
    try:
        usuarios = filter(lambda user:user.id==id,Usuarios)
        return list(usuarios)[0]
    except:
        return {"error":"no se ha encontrado el usuario"}

@router.get("/item/{item_id}")# Query
#http://127.0.0.1:8000/item/3?q=Snilk
#R: {"item_id":3,"q":"Snilk"}
#q es opcional
#http://127.0.0.1:8000/item/3
#{"item_id":3,"q":null}
async def leer_item(item_id:int, q:str = None):
    return {"item_id":item_id, "q":q}


