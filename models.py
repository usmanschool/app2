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
	__tablename__ = 'accounts'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(100), unique=True)
	password = db.Column(db.String(100))

	
	def __init__ (self,username,password):
		self.username = username
		self.password = password

		
		
		
		
class zonetable(UserMixin,db.Model):
	__tablename__ = 'zonetable'
	zoneid = db.Column(db.Integer, primary_key=True)
	uid = db.Column(db.Integer)
	zonename = db.Column(db.String(100))
	bulbid = db.Column(db.String(100))
	brightnesssetting = db.Column(db.Integer)
	lightsensorid = db.Column(db.Integer)
	overrideflag = db.Column(db.Integer)
	energysavingmode = db.Column(db.Integer)
	zonebrightnesslowerbound = db.Column(db.Integer)
	zonebrightnessupperbound = db.Column(db.Integer)


	
	def __init__ (self,uid,zonename,bulbid,brightnesssetting,lightsensorid,overrideflag,energysavingmode,zonebrightnesslowerbound,zonebrightnessupperbound):
		self.uid = uid
		self.zonename = zonename
		self.bulbid = bulbid
		self.brightnesssetting = brightnesssetting
		self.lightsensorid = lightsensorid
		self.overrideflag = overrideflag
		self.energysavingmode = energysavingmode
		self.zonebrightnesslowerbound =  zonebrightnesslowerbound
		self.zonebrightnessupperbound = zonebrightnessupperbound
		

		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		