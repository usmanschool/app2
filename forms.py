#add all of the forms here..... (basically collections of data.)


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField,IntegerField,SelectField

from wtforms.validators import InputRequired, Length,NumberRange,DataRequired


class AddZoneForm(FlaskForm):
	#ZoneId = IntegerField('zoneid')
	ZoneName = StringField('Zone Name', validators=[InputRequired(), Length(min=1, max=100)])
	BulbID = StringField ('Bulb ID(s) in Use', validators=[InputRequired(), Length(min=1, max=100)])
	LightSensorId = IntegerField ('Light Sensor ID',validators=[InputRequired()])
	zonebrightnesslowerbound = IntegerField ('Minimum Lighting Level',validators = [InputRequired(), NumberRange(min=0, max=250)])
	zonebrightnessupperbound = IntegerField ('Maximum Lighting Level',validators = [InputRequired(), NumberRange(min=0, max=250)])
	

class AdjustBrightnessForm(FlaskForm):
	#Override = IntegerField ('Override On/Off',validators = [InputRequired(), NumberRange(min=0, max=1)])
	Override = SelectField('Manual Mode',coerce=int, choices=[(0,"Off"),(1,"On")])
	
	Brightness = IntegerField ('Brightness',validators = [InputRequired(), NumberRange(min=0, max=255)])
	
	
class LoginForm(FlaskForm):
	username = StringField('Username', validators=[InputRequired(), Length(min=1, max=100)])
	password = PasswordField('Password', validators=[InputRequired(), Length(min=1, max=100)])

class RegisterForm(FlaskForm):
	username = StringField('Username', validators=[InputRequired(), Length(min=1, max=100)])
	password = PasswordField('Password', validators=[InputRequired(), Length(min=1, max=100)]) 