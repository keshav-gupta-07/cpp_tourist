from flask import Flask, render_template
from application.database import db
from application.models import *

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config['secret_key'] = 'sdkvnksjn'
app.config['sqlalchemy_database_url'] = 'sqlite:///database.sqlite3'

db.init_app(app)

with app.app_context():
    db.create_all()
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 