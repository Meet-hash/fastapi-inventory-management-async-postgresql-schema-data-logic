from fastapi import FastAPI, Depends, HTTPException
from typing import List
from . import models, crud, database
from .schemas import ProductCreate, ProductRead

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/products/", response_model=ProductRead)
async def add_product(product: ProductCreate):
    return await crud.create_product(product)

@app.get("/products/", response_model=List[ProductRead])
async def list_products():
    return await crud.get_products()
