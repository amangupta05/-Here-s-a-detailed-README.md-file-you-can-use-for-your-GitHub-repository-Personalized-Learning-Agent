from flask import Flask
from config.config import config

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change to a secure key in production

# Import routes
from app.routes import *