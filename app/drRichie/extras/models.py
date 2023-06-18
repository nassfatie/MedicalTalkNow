
from .extensions import db
from datetime import datetime
from flask_login import UserMixin
import enum



class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    first_name = db.Column(db.String(), nullable=False, unique=False)
    last_name = db.Column(db.String(), nullable=False, unique=False)
    username = db.Column(db.String(), nullable=False, unique=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    hashed_password = db.Column(db.String(), nullable=False)
    gender = db.Column(db.String(), nullable=False)
    birth_data = db.Column(db.Date, nullable=False)
    city = db.Column(db.String(), nullable=False, unique=False)
    height = db.Column(db.Integer(), nullable=False)
    weight = db.Column(db.Integer(), nullable=False)
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.profile_pic}')"
    

    
