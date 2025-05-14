from flask import Flask

from src.main.routes.products_routes import products_routes_bp
from src.models.redis.settings.connection import RedisConnection
from src.models.sqlite.settings.connection import SQLiteConnectionHandler

redis_connection = RedisConnection()
sqlite_connection = SQLiteConnectionHandler()
redis_connection.connect()
sqlite_connection.connect()

app = Flask(__name__)
app.register_blueprint(products_routes_bp)
