from redis import Redis


class RedisRepository:
    def __init__(self, redis_conn: Redis) -> None:
        self.__redis_conn = redis_conn

    def insert(self, key: str, value: any) -> None:
        self.__redis_conn.set(key, value)

    def get_key(self, key: str) -> str:
        value = self.__redis_conn.get(key)
        if not value:
            return None
        return value.decode("utf-8")

    def insert_hash(self, key: str, field: str, value: any) -> None:
        self.__redis_conn.hset(key, field, value)

    def get_hash(self, key: str, field: str) -> any:
        value = self.__redis_conn.hget(key, field)
        if not value:
            return None
        return value.decode("utf-8")

    def insert_expire(self, key: str, value: any, expire: int) -> None:
        self.__redis_conn.set(key, value, ex=expire)

    def insert_hash_expire(self, key: str, field: str, value: any, expire: int) -> None:
        self.__redis_conn.hset(key, field, value)
        self.__redis_conn.expire(key, expire)
