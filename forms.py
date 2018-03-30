#add all of the forms here..... (basically collections of data.)


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField,IntegerField

from wtforms.validators import InputRequired, Length,NumberRange


class AddZoneForm(FlaskForm):
	#ZoneId = IntegerField('zoneid')
	ZoneName = StringField('Zone Name', validators=[InputRequired(), Length(min=1, max=100)])
	BulbID = StringField ('List of Bulb IDs present in the zone', validators=[InputRequired(), Length(min=1, max=100)])
	LightSensorId = IntegerField ('Light Sensor ID',validators=[InputRequired()])
	zonebrightnesslowerbound = IntegerField ('Zone Lowest Brightness',validators = [InputRequired(), NumberRange(min=0, max=250)])
	zonebrightnessupperbound = IntegerField ('Zone Maximum Brightness',validators = [InputRequired(), NumberRange(min=0, max=250)])
	

class AdjustBrightnessForm(FlaskForm):
	Override = IntegerField ('Override On/Off',validators = [InputRequired(), NumberRange(min=0, max=1)])
	Brightness = IntegerField ('Brightness',validators = [InputRequired(), NumberRange(min=0, max=255)])
	
	
class LoginForm(FlaskForm):
	username = StringField('Username', validators=[InputRequired(), Length(min=1, max=100)])
	password = PasswordField('Password', validators=[InputRequired(), Length(min=1, max=100)])

class RegisterForm(FlaskForm):
	username = StringField('Username', validators=[InputRequired(), Length(min=1, max=100)])
	password = PasswordField('Password', validators=[InputRequired(), Length(min=1, max=100)]) 