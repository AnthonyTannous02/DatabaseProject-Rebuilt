from flask import render_template,redirect,url_for
from home_page import bp
from flask_login import current_user

@bp.route("/")
@bp.route("/home")
def index():
    user_loggedin = current_user.get_id() != None
    if user_loggedin:
        order_link = url_for('main.rest')
    else:
        order_link = url_for('auth.acc', setting='login')
        
    return render_template("index.html", order_link=order_link) 


@bp.route('/base')
def base():
    return render_template("base.html")  #navbar
