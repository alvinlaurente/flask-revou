"""Pokemon routes"""
from flask import Blueprint
from app.controllers.animal_controller import (
    create_animal,
    get_animal,
    list_animals,
    edit_animal,
    delete_animal
)

animal_blueprint = Blueprint('animal_blueprint', __name__)

animal_blueprint.route("/", methods=["GET"])(list_animals) # type: ignore
animal_blueprint.route("/<string:animal_id>", methods=["GET"])(get_animal) # type: ignore
animal_blueprint.route("/", methods=["POST"])(create_animal) # type: ignore
animal_blueprint.route("/<string:animal_id>", methods=["PUT"])(edit_animal) # type: ignore
animal_blueprint.route("/<string:animal_id>", methods=["DELETE"])(delete_animal) # type: ignore
