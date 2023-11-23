import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

load_dotenv()

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db = SQLAlchemy(app)

migrate = Migrate(app, db)  # Inicializa Flask-Migrate

from controllers.models_folder.models import products
from controllers.models_folder.models import users

with app.app_context():
    db.create_all()

from routes.product_routes import product_routes
from routes.user_routes import user_routes
app.register_blueprint(product_routes)
app.register_blueprint(user_routes)