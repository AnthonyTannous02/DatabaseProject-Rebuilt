from flask import Blueprint, url_for
import jinja2

bp = Blueprint('home', __name__, template_folder='templates/home', static_folder='static/home')

from home_page import routes

