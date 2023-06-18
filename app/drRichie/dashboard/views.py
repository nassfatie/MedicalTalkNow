from flask import g, Blueprint, render_template, request, jsonify, redirect, url_for
from flask_login import login_required
from drRichie.extras.models import User
from flask_login import current_user
from datetime import datetime
from drRichie.extras.extensions import db

dash = Blueprint('dash',__name__,url_prefix='/app')

@dash.route('/dashoard', methods=['GET', 'POST'])
@login_required
def dashboard():
    """This will display user summary"""
    #user = User.query.filter_by(email=email).first_or_404(description='There is no data with {}'.format(email))
    return render_template('dashboard/dashboard.html', title='Dashboard')
@dash.route('/edit', methods=['GET','POST'])
@login_required
def edit():
    return render_template('dashboard/profile.html', title='Edit')

@dash.route('/update/<int:user_id>', methods=['GET','POST'])
@login_required
def update(user_id):
    """This will display user details"""
 
    if request.method == "POST":
        user = User.query.filter_by(id=user_id).first()
        if user:
            user.first_name = request.form.get('first_name')
            user.last_name = request.form.get('last_name')
            user.username = request.form.get('username')
            user.email = request.form.get('email')
            user.gender = request.form.get('gender')
            user.city = request.form.get('city')
            user.height = request.form.get('height')
            user.weight = request.form.get('weight')
            #user.update(dict(first_name=first_name,last_name=last_name,username=username,email=email,gender=gender,city=city,height=height,weight=weight))
            db.session.commit()
            return redirect(url_for('dash.dashboard'))
    

@dash.route('/room', methods=['GET', 'POST'])
@login_required
def room():
    """This will display user details"""
    return render_template('dashboard/room.html', title='Room')

@dash.route('/chat', methods=['GET', 'POST'])
@login_required
def chat():
    """chat function"""
    from drRichie.chatBot.chat import get_response
    text = request.get_json().get("content")
    response = get_response(text)
    message = {"answer":response}
    return jsonify(message)