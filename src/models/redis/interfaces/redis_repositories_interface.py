from abc import ABC, abstractmethod


class RedisRepositoryInterface(ABC):
    @abstractmethod
    def insert(self, key: str, value: any) -> None:
        pass

    @abstractmethod
    def get_key(self, key: str) -> str:
        pass

    @abstractmethod
    def insert_hash(self, key: str, field: str, value: any) -> None:
        pass

    @abstractmethod
    def get_hash(self, key: str, field: str) -> any:
        pass

    @abstractmethod
    def insert_expire(self, key: str, value1: any, value2: any, expire: int) -> None:
        pass

    @abstractmethod
    def insert_hash_expire(self, key: str, field: str, value: any, expire: int) -> None:
        pass
