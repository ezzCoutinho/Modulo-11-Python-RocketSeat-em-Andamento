from flask import Blueprint, jsonify


products_routes_bp = Blueprint("products_routes", __name__)


@products_routes_bp.route("/products", methods=["POST"])
def insert_product():
    return jsonify({"message": "Product inserted successfully"}), 201


@products_routes_bp.route("/products/<string:product_name>", methods=["GET"])
def get_product(product_name: str):
    return jsonify({"message": f"Product {product_name} retrieved successfully"}), 200
