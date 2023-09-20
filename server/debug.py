#!/usr/bin/env python3

from flask import jsonify, request
from app import app, db
from models import Plant

@app.route('/plants', methods=['GET'])
def index():
    plants = Plant.query.all()
    plant_list = [{"id": plant.id, "name": plant.name, "image": plant.image, "price": plant.price} for plant in plants]
    return jsonify(plant_list)

@app.route('/plants/<int:id>', methods=['GET'])
def show(id):
    plant = Plant.query.get(id)
    if plant:
        return jsonify({"id": plant.id, "name": plant.name, "image": plant.image, "price": plant.price})
    else:
        return jsonify({"error": "Plant not found"}), 404

@app.route('/plants', methods=['POST'])
def create():
    data = request.get_json()
    name = data.get("name")
    image = data.get("image")
    price = data.get("price")

    if name and image and price:
        plant = Plant(name=name, image=image, price=price)
        db.session.add(plant)
        db.session.commit()
        return jsonify({"id": plant.id, "name": plant.name, "image": plant.image, "price": plant.price}), 201
    else:
        return jsonify({"error": "Invalid data"}), 400
