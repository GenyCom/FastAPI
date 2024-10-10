from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float

# Liste de produits en memoire (a remplacer par une base de donnees en production)
products = [
    Product(id=1, name="Produit A", description="Description du produit A", price=19.99),
    Product(id=2, name="Produit B", description="Description du produit B", price=29.99),
]

@app.get("/products")
async def get_products():
    return products

@app.get("/products/{product_id}")
async def get_product(product_id: int):
    product = next((p for p in products if p.id == product_id), None)
    if product is None:
        raise HTTPException(status_code=404, detail="Produit non trouve")
    return product