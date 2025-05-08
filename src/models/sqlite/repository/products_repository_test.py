import pytest

from src.models.sqlite.repository.products_repository import ProductsRepository
from src.models.sqlite.settings.connection import db_connection_handler

conn = db_connection_handler.connect()


@pytest.mark.skip(reason="Integration test OK!")
def test_insert_product():
    products_repository = ProductsRepository(conn)
    products_repository.insert_product("I sewar", 9999999.99, 1)
    product = products_repository.find_product_by_name("I sewar")
    assert product is not None
    assert product[1] == "I sewar"
    assert product[2] == 9999999.99
    assert product[3] == 1


@pytest.mark.skip(reason="Integration test OK!")
def test_find_product_by_name():
    products_repository = ProductsRepository(conn)
    product = products_repository.find_product_by_name("I sewar")
    print(product)
    assert product is not None
    assert product[1] == "I sewar"
    assert product[2] == 9999999.99
    assert product[3] == 1
