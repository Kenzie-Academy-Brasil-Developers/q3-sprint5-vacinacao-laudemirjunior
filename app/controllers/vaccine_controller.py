from flask import  jsonify, request, current_app
from app.models.vaccine_model import Vaccine
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError

class ErrorType(Exception):
    pass

def verify_values(data):
    for key in data:
        if type(key) != str:
            raise TypeError


def post_vaccinations():
    try:
        data = request.get_json()

        if len(data["cpf"]) != 11 or data["cpf"].isdigit() == False:
            return {"error": "The CPF field must contain 11 numeric digits"}, HTTPStatus.BAD_REQUEST 

        verify_values(data)     

        new_data = {
        "cpf": data["cpf"],
        "name": data["name"].lower(),
        "vaccine_name": data["vaccine_name"].lower(),
        "health_unit_name": data["health_unit_name"].lower()}
        
        vaccine = Vaccine(**new_data)

        current_app.db.session.add(vaccine)

        current_app.db.session.commit()

        return jsonify(vaccine), HTTPStatus.CREATED

    except (TypeError, AttributeError):
        return {"error": "Fields must contain only strings"}, HTTPStatus.BAD_REQUEST  

    except IntegrityError:
        return {"error": "The CPF entered already exists"}, HTTPStatus.CONFLICT

    except KeyError:
        return {"error": "One or more keys sent are incorrect"}, HTTPStatus.BAD_REQUEST

    
def get_vaccines():
    vaccines = (
      Vaccine
      .query
      .all()
    )

    return jsonify(vaccines), HTTPStatus.OK