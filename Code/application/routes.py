from application.models import User
from application.variables import *
from application import app
from flask import redirect, render_template, request, url_for
from application.database import db

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET','POST'])
def register():
    '''
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if password!= confirm_password:
            return render_template('register.html', error='Passwords do not match')
        else:
            new_user = User(name=name, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            return render_template('register.html', success='You have successfully registered')
    ''' 

    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        password = request.form['password']
        address = request.form['address']
        #role = request.form['role']
        user = User(name, phone, email, password, address, CUSTOMER)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', success='You have successfully registered')

@app.route('/login', methods=['GET','POST'])
def login():
    '''
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error='Invalid email or password')
    '''
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user:
            return redirect(url_for('index'))
    return render_template('login.html', error='Invalid email or password')