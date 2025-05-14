from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.models.redis.interfaces.redis_repositories_interface import (
    RedisRepositoryInterface,
)
from src.models.sqlite.interfaces.sqlite_products_repository_interface import (
    SQLiteProductsRepositoryInterface,
)


class ProductCreator:
    def __init__(
        self,
        redis_repo: RedisRepositoryInterface,
        sqlite_repo: SQLiteProductsRepositoryInterface,
    ) -> None:
        self.__redis_repo = redis_repo
        self.__sqlite_repo = sqlite_repo

    def create(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body

        name = body.get("name")
        price = body.get("price")
        quantity = body.get("quantity")

        self.__insert_in_sql(name, price, quantity)
        self.__insert_in_cache(name, price, quantity)

        return self.__format_response(name, price, quantity)

    def __insert_in_sql(self, name: str, price: float, quantity: int) -> None:
        self.__sqlite_repo.insert_product(name, price, quantity)

    def __insert_in_cache(self, name: str, price: float, quantity: int) -> None:
        self.__redis_repo.insert_expire(name, price, quantity, expire=60)

    def __format_response(self, name: str, price: float, quantity: int) -> HttpResponse:
        return HttpResponse(
            body={
                "type": "Product",
                "count": 1,
                "attributes": {
                    "name": name,
                    "price": price,
                    "quantity": quantity,
                },
            },
            status_code=201,
        )
