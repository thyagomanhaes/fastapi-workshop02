from fastapi import FastAPI
from typing import List, Dict

app = FastAPI() # Create an app instance

products: List[Dict[str, any]] = [
    {
        "id": 1, 
        "name": "Notebook",   
        "price": 1000.00
    },
    {
        "id": 2, 
        "name": "Notebook Gamer",   
        "price": 1000.00
    }
]

@app.get("/") # Cria uma rota
async def root():
    return {"message": "Hello World"}


@app.get("/products")
async def get_products():
    return products