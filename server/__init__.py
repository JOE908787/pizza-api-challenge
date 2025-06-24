from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Import and register blueprints
    from .controllers.restaurant_controller import bp as restaurant_bp
    app.register_blueprint(restaurant_bp)

    from .controllers.pizza_controller import bp as pizza_bp
    app.register_blueprint(pizza_bp)

    from .controllers.restaurant_pizza_controller import bp as restaurant_pizza_bp
    app.register_blueprint(restaurant_pizza_bp)

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Not found"}), 404

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"errors": ["Bad request"]}), 400

    @app.errorhandler(ValueError)
    def handle_value_error(error):
        return jsonify({"errors": [str(error)]}), 400

    return app