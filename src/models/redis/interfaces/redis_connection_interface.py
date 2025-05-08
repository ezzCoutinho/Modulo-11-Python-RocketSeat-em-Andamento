from abc import ABC, abstractmethod

from redis import Redis


class RedisConnectionInterface(ABC):
    @abstractmethod
    def connect(self) -> Redis:
        pass

    @abstractmethod
    def get_connection(self) -> Redis:
        pass
