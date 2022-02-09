from flask import Blueprint

from app.controllers.vaccine_controller import get_vaccines, post_vaccinations

bp_vaccine = Blueprint("bp_vaccine", __name__, url_prefix="/vaccinations")

bp_vaccine.post("")(post_vaccinations)

bp_vaccine.get("")(get_vaccines)
