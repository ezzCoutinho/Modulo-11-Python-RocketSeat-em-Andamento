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
