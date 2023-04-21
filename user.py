from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="mi proyecto Fastapi",
    description="creando mi api rest",
    version="0.0.0.0.0.0.0.001")

#-----------------  Iniciar el server  -----------------  
#pyenv local 3.7.4
#python -m venv venv
#.\venv\Scripts\activate
#py -m uvicorn user:app --reload

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

@app.get("/usuarios")
#/usuarios
async def listar_usuarios():
    return Usuarios


@app.get("/usuario/{ide}")# Path
#/usuario/1
async def buscar_usuario(ide:int):
    return buscar_usuario(ide)


@app.get("/usuario/")# Query
#/usuario/?id=1
async def buscar_usuario(id:int):
    return buscar_usuario(id)

@app.post("/usuario/")#creamos un nuevo usuario
async def crear_usuario(usuario:Usuario):
#    return "agregando usuario con Usuario"
    if type( buscar_usuario(usuario.id) ) == Usuario:
        return {"error":"usuario ya existe"}
    else: 
        Usuarios.append(usuario)
            
@app.put("/usuario/")#actualizar un nuevo usuario
async def actualizar_usuario(usuario:Usuario):
    encontrado=False
    for index, consultar_usuario in enumerate(Usuarios):
        if consultar_usuario.id==usuario.id:
            Usuarios[index]=usuario
            encontrado=True
    
    if not encontrado:
        return {"error":"no se ha actualizado el usuario"}


def buscar_usuario(id:int):
    try:
        usuarios = filter(lambda user:user.id==id,Usuarios)
        return list(usuarios)[0]
    except:
        return {"error":"no se ha encontrado el usuario"}

@app.get("/item/{item_id}")# Query
#http://127.0.0.1:8000/item/3?q=Snilk
#R: {"item_id":3,"q":"Snilk"}
#q es opcional
#http://127.0.0.1:8000/item/3
#{"item_id":3,"q":null}
async def leer_item(item_id:int, q:str = None):
    return {"item_id":item_id, "q":q}


