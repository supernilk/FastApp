from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#mecanismos de seguridad para la autenticacion de usuario

#Entidad usuario
class Usuario(BaseModel):
    usuario_nombre:str
    nombre: str
    correo: str
    disable: bool

class Usuario_BD(Usuario):
    usuario_password:str    

db_usuarios = {
        "john":{
            "usuario_nombre":"John",
            "usuario_password":"123",
            "nombre": "Snilk",
            "correo": "nilk.ao@gmail.com",
            "disable": False
        },

        "el_pepe":{
            "usuario_nombre":"super",
            "usuario_password":"456",
            "nombre": "Ramon",
            "correo": "Ramon.pp@gmail.com",
            "disable": True
        },
    }