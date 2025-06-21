# Pizza Restaurant API Challenge

This is a RESTful API for a Pizza Restaurant built using Flask, following the MVC pattern. It provides endpoints to manage restaurants, pizzas, and their relationships via a join table (`RestaurantPizza`).

## Setup Instructions

1. **Clone the Repository**
   
   git clone https://github.com/<your-username>/pizza-api-challenge.git
   cd pizza-api-challenge

Set Up Virtual Environment
pipenv install flask flask_sqlalchemy flask_migrate
pipenv shell

Configure Flask and Database
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

Seed the Database
python server/seed.py

Run the Application
flask run

Database Migration & Seeding
Migration: The flask db commands (init, migrate, upgrade) set up and update the SQLite database (app.db).
Seeding: Run python server/seed.py to populate the database with sample restaurants, pizzas, and their relationships.
Route Summary

Method	Endpoint	Description
GET	/restaurants	List all restaurants
GET	/restaurants/<id>	Get details of a restaurant and its pizzas
DELETE	/restaurants/<id>	Delete a restaurant and its related pizzas
GET	/pizzas	List all pizzas
POST	/restaurant_pizzas	Create a new restaurant-pizza relationship