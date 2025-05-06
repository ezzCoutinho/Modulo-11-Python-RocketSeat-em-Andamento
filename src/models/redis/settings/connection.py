from redis import Redis


class RedisConnection:
    def __init__(self):
        self.__redis = None

    def connect(self) -> Redis:
        conn = Redis(host="localhost", port=6379, db=0)
        self.__redis = conn
        return conn

    def get_connection(self) -> Redis:
        return self.__redis
