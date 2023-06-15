from flask import Blueprint
from flask import render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from drRichie.extras.models import User
from drRichie.extras.extensions import db
from flask_login import login_user, logout_user, login_required


auth = Blueprint('auth', __name__, url_prefix='/')

""""----------register function---------------------------"""
@auth.route('/signup')
def register():
    return render_template('authentication/register.html', title = 'Sign Up')

@auth.route('/signup', methods=['POST'])
def signup():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()
    if user:
        flash('User with that email already exists.')
        return redirect(url_for('auth.signup'))
    else:
        new_user = User(username = username, email = email, hashed_password = generate_password_hash(password, method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth.sign_in'))

""""----------login function---------------------------"""
@auth.route('/')
def sign_in():
    return render_template('authentication/login.html', title = 'Login')

@auth.route('/', methods=["POST"])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()
    if not user and not check_password_hash(user.hashed_password, password):
        flash('Invalid email or password.')
        return redirect(url_for('auth.login'))
    
    from drRichie.dashboard.views import dash
    login_user(user)
    return redirect(url_for('dash.dashboard'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
