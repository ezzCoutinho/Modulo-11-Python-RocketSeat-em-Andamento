from src.models.redis.settings.connection import RedisConnection
from src.models.sqlite.settings.connection import SQLiteConnectionHandler

redis_connection = RedisConnection()
sqlite_connection = SQLiteConnectionHandler()


def initialize_connections():
    redis_connection.connect()
    sqlite_connection.connect()


def get_redis_connection():
    return redis_connection


def get_sqlite_connection():
    return sqlite_connection
