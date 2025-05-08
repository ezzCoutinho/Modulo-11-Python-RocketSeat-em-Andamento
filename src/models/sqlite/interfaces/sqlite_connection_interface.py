from sqlite3 import Connection as SQLiteConnection
from abc import ABC, abstractmethod


class SQLiteConnectionInterface(ABC):
    @abstractmethod
    def connect(self) -> SQLiteConnection:
        pass

    @abstractmethod
    def close(self) -> None:
        pass

    @abstractmethod
    def get_connection(self) -> SQLiteConnection:
        pass
