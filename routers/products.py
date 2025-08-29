from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/products",
    tags=["products"],
    responses={404: {"message": "No encontrado"}})


products_list = ["Producto 1",
                 "Producto 2",
                 "Producto 3",
                 "Producto 4",
                 "Producto 5"]


@router.get("/")
async def get_products():
    return products_list
# Url local: http://127.0.0.1:8000/products


@router.get("/{id}")
async def get_product(id: int):

    if id < 0 or id >= len(products_list):
        raise HTTPException(status_code=404,detail="error: Producto no encontrado.")
    
    return products_list[id]
# Url local: http://127.0.0.1:8000/products/0
# Url local: http://127.0.0.1:8000/products/1
# Url local: http://127.0.0.1:8000/products/2
# Url local: http://127.0.0.1:8000/products/3
# Url local: http://127.0.0.1:8000/products/4
# Url local: http://127.0.0.1:8000/products/5
#   Mensaje: "error": "Producto no encontrado"