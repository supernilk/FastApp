from fastapi import FastAPI

app = FastAPI()

#Iniciar el server: py -m uvicorn main:app --reload

@app.get("/users")
async def users():
    return "Hola Users"
