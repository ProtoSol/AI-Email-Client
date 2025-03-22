# Libraries

from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from transformers import pipeline  # Import the transformer library

# Initialize the libraries

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
mail = Mail()
migrate = Migrate()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e08dd73152b14e7a0c2b7503412534ba'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
bcrypt.init_app(app)
login_manager.init_app(app)
mail.init_app(app)
migrate.init_app(app, db)

# Initialize the summarization pipeline
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from Project import routes
