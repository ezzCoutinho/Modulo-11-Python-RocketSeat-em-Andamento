import sqlite3
from sqlite3 import Connection as SQLiteConnection


class SQLiteConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "settings.db"
        self.__conn = None

    def connect(self) -> SQLiteConnection:
        conn = sqlite3.connect(self.__connection_string, check_same_thread=False)
        self.__conn = conn
        return conn

    def close(self) -> None:
        self.__conn.close()

    def get_connection(self) -> SQLiteConnection:
        return self.__conn


db_connection_handler = SQLiteConnectionHandler()
