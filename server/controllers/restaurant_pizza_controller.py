from flask import Blueprint, request, jsonify
from server.config import db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

bp = Blueprint('restaurant_pizzas', __name__)

@bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    try:
        price = data['price']
        pizza_id = data['pizza_id']
        restaurant_id = data['restaurant_id']

        # Validate price
        if not (1 <= price <= 30):
            return jsonify({'errors': ['Price must be between 1 and 30']}), 400

        # Check if pizza exists
        pizza = Pizza.query.get(pizza_id)
        if not pizza:
            return jsonify({'errors': ['Pizza not found']}), 400

        # Check if restaurant exists
        restaurant = Restaurant.query.get(restaurant_id)
        if not restaurant:
            return jsonify({'errors': ['Restaurant not found']}), 400

        # Create new RestaurantPizza
        restaurant_pizza = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
        db.session.add(restaurant_pizza)
        db.session.commit()

        return jsonify(restaurant_pizza.to_dict()), 201
    except KeyError as e:
        return jsonify({'errors': [f'Missing key: {e.args[0]}']}), 400
    except ValueError as e:
        return jsonify({'errors': [str(e)]}), 400
    except Exception as e:
        return jsonify({'errors': [str(e)]}), 500