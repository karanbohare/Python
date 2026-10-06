import mysql.connector

from app.models.product import Product


class ProductRepository:

    def __init__(self):

        self.connection = mysql.connector.connect(host="localhost", user="root", password="password", database="product_api")

    # GET ALL PRODUCTS
    def get_all(self):

        cursor = self.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()
        cursor.close()
        return [Product(**row) for row in rows]

    # GET PRODUCT BY ID
    def get_by_id(self, product_id: int):

        cursor = self.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM products WHERE product_id = %s", (product_id,))
        row = cursor.fetchone()
        cursor.close()

        if row is None:
            return None

        return Product(**row)

    # CREATE PRODUCT
    def create(self, product_data: dict):

        cursor = self.connection.cursor()
        query = """
            INSERT INTO products
            (product_name, price, description, stock)
            VALUES (%s, %s, %s, %s)
        """

        values = (product_data["product_name"],product_data["price"],product_data["description"],product_data["stock"])

        cursor.execute(query, values) 
        self.connection.commit()
        product_id = cursor.lastrowid
        cursor.close()

        return self.get_by_id(product_id)

    # UPDATE PRODUCT
    def update(self, product_id: int, product_data: dict):

        cursor = self.connection.cursor()

        query = """
            UPDATE products
            SET
                product_name = %s,
                price = %s,
                description = %s,
                stock = %s
            WHERE product_id = %s
        """

        values = (product_data["product_name"],product_data["price"],product_data["description"],product_data["stock"],product_id)  
        cursor.execute(query, values)
        affected_rows = cursor.rowcount
        self.connection.commit()
        cursor.close()

        if affected_rows == 0:
            return None

        return self.get_by_id(product_id)

    # DELETE PRODUCT
    def delete(self, product_id: int):

        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM products WHERE product_id = %s",(product_id,))
        affected_rows = cursor.rowcount
        self.connection.commit()
        cursor.close()

        if affected_rows == 0:
            return None

        return {
            "message": "Product deleted successfully"
        }