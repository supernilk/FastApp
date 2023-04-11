#https://stackoverflow.com/questions/64936440/python-uvicorn-the-term-uvicorn-is-not-recognized-as-the-name-of-a-cmdlet-f
from fastapi import FastAPI

app = FastAPI()

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

#