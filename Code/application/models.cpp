from application.database import db

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(75), nullable=False)
    phone=db.Column(db.String(15), nullable=False, unique=True)
    email=db.Column(db.String(75), nullable=False, unique=True)
    password=db.Column(db.String(75), nullable=False)
    address=db.Column(db.String(75), nullable=False)
    role=db.Column(db.String(75), nullable=False, default='customer')

    def __init__(self, name, phone, email, password, address, role):
        self.name = name
        self.phone = phone
        self.email = email
        self.password = password
        self.address = address
        self.role = role

    def __repr__(self):
        return '<User %r>' % self.name
