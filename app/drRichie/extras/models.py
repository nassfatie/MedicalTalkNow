
from .extensions import db
from datetime import datetime
from flask_login import UserMixin
import enum



class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(), nullable=False, unique=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    hashed_password = db.Column(db.String(), nullable=False)
    joined_at = db.Column(db.DateTime(), default = datetime.utcnow, index = True)
    patient_id = db.Column(db.Integer(), db.ForeignKey('patients.patient_id'))
    #profile_pic = db.Column(db.String(), nullable=False, default='default.jpg')
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.profile_pic}')"
    
class Patient(db.Model):
    __tablename__ = "patients"
    class Gender(enum.Enum):
        female = 0
        male = 1
        other = 2

    patient_id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(), nullable=False, unique=False)
    last_name = db.Column(db.String(), nullable=False, unique=False)
    gender = db.Column(db.Enum(Gender), nullable=False)
    birth_data = db.Column(db.DateTime, nullable=False)
    city = db.Column(db.String(), nullable=False, unique=False)
    height = db.Column(db.Integer(), nullable=False)
    weight = db.Column(db.Integer(), nullable=False)
    username = db.relationship('User', uselist=False, backref='Patient_username', lazy=True)
    def __repr__(self):
        return f"User('{self.first_name}', '{self.last_name}','{self.birth_data}')"

    
