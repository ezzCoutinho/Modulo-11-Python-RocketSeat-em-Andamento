from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.models.redis.interfaces.redis_repositories_interface import (
    RedisRepositoryInterface,
)
from src.models.sqlite.interfaces.sqlite_products_repository_interface import (
    SQLiteProductsRepositoryInterface,
)


class ProductFinder:
    def __init__(
        self,
        redis_repo: RedisRepositoryInterface,
        sqlite_repo: SQLiteProductsRepositoryInterface,
    ) -> None:
        self.__redis_repo = redis_repo
        self.__sqlite_repo = sqlite_repo

    def find_by_name(self, http_request: HttpRequest) -> HttpResponse:
        product_name = http_request.params.get("product_name")
        product = None
        product = self.__find_in_cache(product_name)

        if not product:
            product = self.__find_in_sql(product_name)
            self.__insert_in_cache(product)

        return self.__format_response(product)

    def __find_in_cache(self, product_name: str) -> tuple:
        product_info = self.__redis_repo.get_key(product_name)

        if product_info:
            product_info_list = product_info.split(",")
            return (0, product_name, product_info_list[0], product_info_list[1])

        return None

    def __find_in_sql(self, product_name: str) -> tuple:
        product_info = self.__sqlite_repo.find_product_by_name(product_name)

        if not product_info:
            raise Exception("Product not found")

        return product_info

    def __insert_in_cache(self, product: tuple) -> None:
        product_name = product[1]
        value = f"{product[2]},{product[3]}"
        self.__redis_repo.insert_expire(product_name, value, 60)

    def __format_response(self, product: tuple) -> HttpResponse:
        return HttpResponse(
            body={
                "type": "Product",
                "count": 1,
                "attributes": {
                    "name": product[1],
                    "price": product[2],
                    "quantity": product[3],
                },
            },
            status_code=200,
        )
