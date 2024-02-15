"""Pokemon controller"""
from http.client import CREATED, INTERNAL_SERVER_ERROR, NOT_FOUND, OK
from flask import jsonify, request
from app.db.config import db
from app.models.animal import Animal

def list_animals():
    """GET ANIMAL LIST"""
    try:
        animals = Animal.query.all()
        return [animal.as_dict() for animal in animals], OK
    except Exception as e:
        return e, INTERNAL_SERVER_ERROR

def get_animal(animal_id: str):
    """GET ANIMAL BY ID"""
    try:
        animal = Animal.query.get(animal_id)

        if animal:
            # If the animal with the specified ID exists
            return jsonify({
                "id": animal.id,
                "name": animal.name,
                "binomial_name": animal.binomial_name,
                "genus": animal.genus,
                "family": animal.family,
                "order": animal.order,
                "class": animal.class_column,
                "phylum": animal.phylum
            }), OK
        return jsonify({'error': 'Animal not found'}), NOT_FOUND
    except Exception as e:
        return e, INTERNAL_SERVER_ERROR

def create_animal():
    """CREATE NEW ANIMAL"""
    try:
        data = request.json
        animal = Animal()

        if data is not None:
            animal.name = data["name"]
            animal.binomial_name = data["binomial_name"]
            animal.genus = data["genus"]
            animal.family = data["family"]
            animal.order = data["order"]
            animal.class_column = data["class"]
            animal.phylum = data["phylum"]

        db.session.add(animal)
        db.session.commit()

        return jsonify('success'), CREATED
    except Exception as e:
        return jsonify({'error': str(e)}), INTERNAL_SERVER_ERROR

def edit_animal(animal_id: str):
    """EDIT ANIMAL BY ID"""
    try:
        animal = Animal.query.get(animal_id)

        if animal is None:
            return jsonify({'error': 'Animal not found'}), NOT_FOUND

        data = request.json
        if data is not None:
            animal.name = data.get('name', animal.name)
            animal.binomial_name = data.get('binomial_name', animal.binomial_name)
            animal.genus = data.get('genus', animal.genus)
            animal.family = data.get('family', animal.family)
            animal.order = data.get('order', animal.order)
            animal.class_column = data.get('class', animal.class_column)
            animal.phylum = data.get('phylum', animal.phylum)

        db.session.commit()

        return jsonify({'message': 'Animal updated successfully'}), OK
    except Exception as e:
        return jsonify({'error': str(e)}), INTERNAL_SERVER_ERROR

def delete_animal(animal_id: str):
    """DELETE ANIMAL BY ID"""
    try:
        animal = Animal.query.get(animal_id)

        if animal is None:
            return jsonify({'error': 'Animal not found'}), NOT_FOUND

        db.session.delete(animal)
        db.session.commit()

        return jsonify({'message': 'Animal deleted successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), INTERNAL_SERVER_ERROR
