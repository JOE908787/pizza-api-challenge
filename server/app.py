from flask import Flask
from server.config import app, db
from server.controllers import restaurant_controller, pizza_controller, restaurant_pizza_controller

# Initialize Flask app and register blueprints
app.register_blueprint(restaurant_controller.bp)
app.register_blueprint(pizza_controller.bp)
app.register_blueprint(restaurant_pizza_controller.bp)

if __name__ == '__main__':
    app.run(debug=True)
   