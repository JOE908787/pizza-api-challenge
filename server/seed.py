from server.models import db, Restaurant, Pizza, RestaurantPizza
from server.app import app

with app.app_context():
    # Clear old data (optional for development)
    RestaurantPizza.query.delete()
    Restaurant.query.delete()
    Pizza.query.delete()

    # Create pizzas
    pizza1 = Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Cheese")
    pizza2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")

    # Create restaurants
    r1 = Restaurant(name="Pizza Palace", address="123 Main St")
    r2 = Restaurant(name="Kiki's Pizza", address="456 Elm St")

    db.session.add_all([pizza1, pizza2, r1, r2])
    db.session.commit()

    # Link them through RestaurantPizza
    rp1 = RestaurantPizza(price=10, pizza_id=pizza1.id, restaurant_id=r1.id)
    rp2 = RestaurantPizza(price=15, pizza_id=pizza2.id, restaurant_id=r2.id)

    db.session.add_all([rp1, rp2])
    db.session.commit()

    print("✅ Database seeded!")
