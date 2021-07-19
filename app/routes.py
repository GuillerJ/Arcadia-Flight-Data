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
    tocho = {
  "draw": 7,
  "recordsTotal": 57,
  "recordsFiltered": 57,
  "data": [
    {
      "0": "Airi",
      "1": "Satou",
      "2": "Accountant",
      "3": "Tokyo",
      "4": "28th Nov 08",
      "5": "$162,700",
      "DT_RowId": "row_5"
    },
    {
      "0": "Angelica",
      "1": "Ramos",
      "2": "Chief Executive Officer (CEO)",
      "3": "London",
      "4": "9th Oct 09",
      "5": "$1,200,000",
      "DT_RowId": "row_25"
    },
    {
      "0": "Ashton",
      "1": "Cox",
      "2": "Junior Technical Author",
      "3": "San Francisco",
      "4": "12th Jan 09",
      "5": "$86,000",
      "DT_RowId": "row_3"
    },
    {
      "0": "Bradley",
      "1": "Greer",
      "2": "Software Engineer",
      "3": "London",
      "4": "13th Oct 12",
      "5": "$132,000",
      "DT_RowId": "row_19"
    },
    {
      "0": "Brenden",
      "1": "Wagner",
      "2": "Software Engineer",
      "3": "San Francisco",
      "4": "7th Jun 11",
      "5": "$206,850",
      "DT_RowId": "row_28"
    },
    {
      "0": "Brielle",
      "1": "Williamson",
      "2": "Integration Specialist",
      "3": "New York",
      "4": "2nd Dec 12",
      "5": "$372,000",
      "DT_RowId": "row_6"
    },
    {
      "0": "Bruno",
      "1": "Nash",
      "2": "Software Engineer",
      "3": "London",
      "4": "3rd May 11",
      "5": "$163,500",
      "DT_RowId": "row_43"
    },
    {
      "0": "Caesar",
      "1": "Vance",
      "2": "Pre-Sales Support",
      "3": "New York",
      "4": "12th Dec 11",
      "5": "$106,450",
      "DT_RowId": "row_23"
    },
    {
      "0": "Cara",
      "1": "Stevens",
      "2": "Sales Assistant",
      "3": "New York",
      "4": "6th Dec 11",
      "5": "$145,600",
      "DT_RowId": "row_51"
    },
    {
      "0": "Cedric",
      "1": "Kelly",
      "2": "Senior Javascript Developer",
      "3": "Edinburgh",
      "4": "29th Mar 12",
      "5": "$433,060",
      "DT_RowId": "row_4"
    }
  ]
}
    return tocho

@app.before_request
def before_request():

    if current_user.is_authenticated:
        current_user.ultimaConexion = datetime.now()
        db.session.commit()
