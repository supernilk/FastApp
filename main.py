from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "hola FastApp"

#para ejecutar:
#en caso de que no funcione con uvicorn main:app --reload
#python -m uvicorn main:app --reload