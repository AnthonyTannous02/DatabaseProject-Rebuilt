from flask import Blueprint

bp = Blueprint('auth', __name__, template_folder="templates/auth", static_folder='static/auth')


from auth_page import routes, email_conf