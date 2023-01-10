from flask import Blueprint

bp = Blueprint('main', __name__, template_folder="templates/main", static_folder='static/main')

from main_page import routes