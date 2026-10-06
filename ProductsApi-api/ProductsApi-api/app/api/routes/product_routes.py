from fastapi import APIRouter, HTTPException, Request

from app.schemas.product_schema import (
    ProductCreate,
    ProductUpdate,
    ProductResponse
)


router = APIRouter(
    prefix="/api/products",
    tags=["Products"]
)


# GET ALL PRODUCTS
@router.get("/", response_model=list[ProductResponse])
def get_all_products(request: Request):

    service = request.app.state.product_service

    products = service.get_all_products()

    return [
        {
            "id": product.product_id,
            "product_name": product.product_name,
            "description": product.description,
            "price": product.price,
            "stock": product.stock
        }
        for product in products
    ]


# GET PRODUCT BY ID
@router.get("/{product_id}", response_model=ProductResponse)
def get_product_by_id(
    product_id: int,
    request: Request
):

    service = request.app.state.product_service

    product = service.get_product_by_id(product_id)

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return {
        "id": product.product_id,
        "product_name": product.product_name,
        "description": product.description,
        "price": product.price,
        "stock": product.stock
    }


# CREATE PRODUCT
@router.post("/", response_model=ProductResponse)
def create_product(
    product: ProductCreate,
    request: Request
):

    service = request.app.state.product_service

    result = service.create_product(
        product.model_dump()
    )

    return {
        "id": result.product_id,
        "product_name": result.product_name,
        "description": result.description,
        "price": result.price,
        "stock": result.stock
    }


# UPDATE PRODUCT
@router.put("/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: int,
    product: ProductUpdate,
    request: Request
):

    service = request.app.state.product_service

    result = service.update_product(
        product_id,
        product.model_dump()
    )

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return {
        "id": result.product_id,
        "product_name": result.product_name,
        "description": result.description,
        "price": result.price,
        "stock": result.stock
    }


# DELETE PRODUCT
@router.delete("/{product_id}")
def delete_product(
    product_id: int,
    request: Request
):

    service = request.app.state.product_service

    result = service.delete_product(product_id)

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return result