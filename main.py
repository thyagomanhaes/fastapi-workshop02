from fastapi import FastAPI

app = FastAPI() # Cria uma instância do app

@app.get("/") # Cria uma rota
async def root():
    return {"message": "Hello World"}
