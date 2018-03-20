from flask_sqlalchemy import SQLAlchemy

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

