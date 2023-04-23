#https://stackoverflow.com/questions/64936440/python-uvicorn-the-term-uvicorn-is-not-recognized-as-the-name-of-a-cmdlet-f
from fastapi import FastAPI
from routers import productos, user


app = FastAPI(
    title="mi proyecto Fastapi",
    description="creando mi api rest",
    version="0.0.0.0.0.0.0.001")

# Routers
app.include_router(productos.router)
app.include_router(user.router)

@app.get("/")
async def root():
    return "Hola FastApp"

@app.get("/url")
async def url():
    return {"url_curso": "https://mouredev.com/python"}
#Iniciar el server: uvicorn main:app --reload
#En caso de que no funcione: py -m uvicorn main:app --reload
#Detener el server: CTRL+C

#Documentacion con Swagger: http://127.0.0.1:8000/docs
#Documentacion con Redocly: http://127.0.0.1:8000/redoc

# --------- CRUD --------- #
#Post:   para crear datos.
#Get:    para leer datos.
#Put:    para actualizar datos.
#Delete: para eliminar datos