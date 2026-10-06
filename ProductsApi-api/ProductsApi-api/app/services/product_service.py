from app.repositories.product_repository import ProductRepository


class ProductService:

    def __init__(self, repository: ProductRepository):

        self.repository = repository

    # GET ALL PRODUCTS
    def get_all_products(self):

        return self.repository.get_all()

    # GET PRODUCT BY ID
    def get_product_by_id(self, product_id: int):

        return self.repository.get_by_id(product_id)

    # CREATE PRODUCT
    def create_product(self, product_data: dict):

        return self.repository.create(product_data)

    # UPDATE PRODUCT
    def update_product(self, product_id: int, product_data: dict):

        return self.repository.update(product_id, product_data)

    # DELETE PRODUCT
    def delete_product(self, product_id: int):

        return self.repository.delete(product_id)