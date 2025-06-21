from flask import Blueprint, jsonify
from server.models.pizza import Pizza

bp = Blueprint('pizzas', __name__)

@bp.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([pizza.to_dict() for pizza in pizzas])