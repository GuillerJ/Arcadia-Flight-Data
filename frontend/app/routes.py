from flask import render_template, request
from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from datetime import datetime
import requests

from app import app, db
from app.modelos import Usuario
from app.formularios import LoginForm, RegistrationForm, EditProfileForm
api_url = 'http://localhost:5005/{}'
api_key = 'gjv_apiKey'



@app.route('/')
@app.route('/index')
@login_required
def index():
    airports = requests.get(api_url.format('exAir'), headers={"api-key":api_key}).json()
    return render_template("index.html", title='Home Page', user=current_user, airports=airports)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Usuario.query.filter_by(usuario=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = Usuario(usuario=form.username.data, correo=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/load/airports')
def a_airports():
    airport = request.args.get('airport')
    date = request.args.get('date')
    arrivals = requests.get(api_url.format('arrivals/{}/{}'.format(airport, date)), headers={"api-key":api_key}).json()

    return arrivals

@app.before_request
def before_request():

    if current_user.is_authenticated:
        current_user.ultimaConexion = datetime.now()
        db.session.commit()
