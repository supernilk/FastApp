from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#-----------------  Iniciar el server  -----------------  
#pyenv local 3.7.4
#python -m venv venv
#.\venv\Scripts\activate
#py -m uvicorn user:app --reload


#Entidad usuario
class Usuario(BaseModel):
    id: int
    nombre: str
    apellido: str
    url: str
    edad: int

#lista que puede provenir de una base de datos
Usuarios = [Usuario(id=1, nombre="John", apellido="Barragan", url="html://google.co.ve",edad=45),
            Usuario(id=2, nombre="Pedro", apellido="Perez", url="html://perez.com",edad=23),
            Usuario(id=3, nombre="ana", apellido="rodriguez", url="html://zorras.us",edad=18)]

@app.get("/usuarios")
async def listar_usuarios():
    return Usuarios


@app.get("/usuario/{ide}")# Path
async def buscar_usuario(ide:int):
    return buscar_usuario(ide)


@app.get("/usuario/")# Query
async def buscar_usuario(id:int):
    return buscar_usuario(id)
    
def buscar_usuario(id:int):
    try:
        usuarios = filter(lambda user:user.id==id,Usuarios)
        return list(usuarios)[0]
    except:
        return {"error":"no se ha encontrado el usuario"}

@app.post("/usuario/")
async def Agregar_usuario():
    return ("agregando usuario")