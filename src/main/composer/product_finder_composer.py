from src.data.product_finder import ProductFinder
from src.main.server.connections import get_redis_connection, get_sqlite_connection
from src.models.redis.repositories.redis_repository import RedisRepository
from src.models.sqlite.repository.products_repository import ProductsRepository


def product_finder_composer() -> ProductFinder:
    redis_connection = get_redis_connection()
    sqlite_connection = get_sqlite_connection()

    redis_conn = redis_connection.get_connection()
    sqlite_conn = sqlite_connection.get_connection()

    redis_repo = RedisRepository(redis_conn)
    sqlite_repo = ProductsRepository(sqlite_conn)

    product_finder = ProductFinder(redis_repo, sqlite_repo)

    return product_finder
