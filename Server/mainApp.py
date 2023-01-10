from flask import Flask, url_for, render_template, request
import mysql.connector
 
#New imports
from flask_session import Session
from flask_login import LoginManager
import secrets


app = Flask(__name__)

app.config["SECRET_KEY"] = secrets.token_hex
app.config["SESSION_TYPE"] = 'filesystem'
app.config["SESSION_FILE_DIR"] = "Server/flask_session"
app.config["PERMANENT_SESSION_LIFETIME"] = 600

#OTP Session
sess = Session(app)
sess.init_app(app)

#Login Manager
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = "auth.acc"

from database import User, Database

@login_manager.user_loader
def load_user(id):
    try:
        return User.create_user(id)
    except:
        return 
    

  
def create_app():
    from home_page import bp as homebp
    from auth_page import bp as testbp
    from main_page import bp as mainbp
    
    app.register_blueprint(homebp)
    app.register_blueprint(testbp, url_prefix='/auth')
    app.register_blueprint(mainbp, url_prefix="/main")
    

    
    return app


if __name__ == "__main__":
    
    create_app().run(debug=True)

