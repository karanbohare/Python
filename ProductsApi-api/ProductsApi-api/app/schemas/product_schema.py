from pydantic import BaseModel, Field

class ProductCreate(BaseModel):
    product_name: str = Field(min_length=2, max_length=100)
    description: str = Field(min_length=2, max_length=100)
    price: float = Field(gt=0)
    stock: int = Field(gt=0)


class ProductUpdate(ProductCreate):
    pass


class ProductResponse(ProductCreate):
    id: int