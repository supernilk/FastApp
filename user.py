from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Iniciar el server: py -m uvicorn main:app --reload

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

@app.get("/usuario/{id}")
async def buscar_usuario(id:int):
    return Usuarios(id)
