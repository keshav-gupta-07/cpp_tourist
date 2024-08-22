from flask import Flask, render_template
from application.database import db
from application.models import *

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config['secret_key'] = 'sdkvnksjn'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'

db.init_app(app)

with app.app_context():
    db.create_all()

