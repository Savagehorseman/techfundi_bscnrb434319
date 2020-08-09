# models.py

from flask_login import UserMixin
from . import db
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
	status = db.Column(db.String(100),default=negative)
	
	
class Contact(db.Model):
    c_id = db.Column(db.Integer, primary_key=True) 
	date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
   
	