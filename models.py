from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


db = SQLAlchemy()

class settings(db.Model):
	__tablename__ = 'settings'
	uid = db.Column(db.Integer, primary_key = True)
	zone = db.Column(db.String(100))	
	bulbid = db.Column(db.String(100))

	def __init__(self,zone,bulbid):
		#self.uid = uid
		self.zone = zone
		self.bulbid = bulbid

		
class accounts(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(100), unique=True)
	password = db.Column(db.String(100))

	
	def __init__ (self,username,password):
		self.username = username
		self.password = password


		
		
