from redis import Redis

from src.models.redis.interfaces.redis_connection_interface import (
    RedisConnectionInterface,
)


class RedisConnection(RedisConnectionInterface):
    def __init__(self):
        self.__redis = None

    def connect(self) -> Redis:
        conn = Redis(host="localhost", port=6379, db=0)
        self.__redis = conn
        return conn

    def get_connection(self) -> Redis:
        return self.__redis
