from flask import Blueprint, jsonify, request
from server.models.pizza import Pizza

bp = Blueprint('pizzas', __name__)

@bp.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    if not pizzas:
        return jsonify({'error': 'Not Found'}), 404
    return jsonify([pizza.to_dict() for pizza in pizzas])

@bp.route('/pizzas/<int:id>', methods=['GET'])
def get_pizza(id):
    pizza = Pizza.query.get(id)
    if not pizza:
        return jsonify({'error': 'Pizza not found'}), 404
    return jsonify(pizza.to_dict())