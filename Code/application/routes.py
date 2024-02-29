from Code.application.models import User
from Code.application.variables import *
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
        role = request.form['role']
        user = User(name, phone, email, password, address, CUSTOMER)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', success='You have successfully registered')