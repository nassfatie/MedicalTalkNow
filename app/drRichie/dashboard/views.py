from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required

dash = Blueprint('dash',__name__,url_prefix='/app')

@dash.route('/dashoard', methods=['GET', 'POST'])
@login_required
def dashboard():
    """This will display user summary"""
    return render_template('dashboard/dashboard.html', title='Dashboard')

@dash.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    """This will display user details"""
    return render_template('dashboard/profile.html', title='profile')

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