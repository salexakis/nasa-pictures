from flask import Flask
from dotenv import load_dotenv
from flask_mailman import Mail, EmailMessage
from flask_cors import CORS
import os

mail = Mail()
cors = CORS()

def create_app():

    app_dir = os.getcwd()
    instance_path = os.path.join(app_dir, 'instance') 
    
    app = Flask(__name__, instance_path=instance_path)
    app.config.from_object('application.config.DevelopmentConfig')
    mail.init_app(app)
    cors.init_app(app)

    from .routes import main

    app.register_blueprint(main)

    return app