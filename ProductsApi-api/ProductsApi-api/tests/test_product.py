from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


# GET ALL PRODUCTS
def test_get_all_products():

    response = client.get("/api/products/")

    assert response.status_code == 200
    assert len(response.json()) >= 3


# GET PRODUCT BY ID
def test_get_product_by_id():

    response = client.get("/api/products/1")

    assert response.status_code == 200
    assert response.json()["id"] == 1


# GET PRODUCT NOT FOUND
def test_get_product_not_found():

    response = client.get("/api/products/100")

    assert response.status_code == 404


# CREATE PRODUCT
def test_create_product():

    product = {
        "product_name": "Mouse",
        "description": "Wireless mouse",
        "price": 1200.0,
        "stock": 50
    }

    response = client.post(
        "/api/products/",
        json=product
    )

    assert response.status_code == 200
    assert response.json()["product_name"] == "Mouse"


# UPDATE PRODUCT
def test_update_product():

    product = {
        "product_name": "Updated Mouse",
        "description": "Updated Product",
        "price": 1500.0,
        "stock": 100
    }

    response = client.put(
        "/api/products/1",
        json=product
    )

    assert response.status_code == 200
    assert response.json()["product_name"] == "Updated Mouse"


# DELETE PRODUCT
def test_delete_product():

    response = client.delete("/api/products/1")

    assert response.status_code == 200