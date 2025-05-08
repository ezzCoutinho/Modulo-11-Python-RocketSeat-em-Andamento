from abc import ABC, abstractmethod


class SQLiteProductsRepositoryInterface(ABC):
    @abstractmethod
    def find_product_by_name(self, product_name: str) -> tuple:
        pass

    def insert_product(self, name: str, price: float, quantity: int) -> None:
        pass
