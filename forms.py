#add all of the forms here..... (basically collections of data.)


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField

from wtforms.validators import InputRequired, Length


class AddZone(FlaskForm):
	ZoneName = StringField('Zone Name')
	BulbID = StringField ('List of Bulb IDs')
	submit = SubmitField ('Create')
	
	
class LoginForm(FlaskForm):
	username = StringField('Username', validators=[InputRequired(), Length(min=1, max=100)])
	password = PasswordField('Password', validators=[InputRequired(), Length(min=1, max=100)])

class RegisterForm(FlaskForm):
	username = StringField('Username', validators=[InputRequired(), Length(min=1, max=100)])
	password = PasswordField('Password', validators=[InputRequired(), Length(min=1, max=100)]) 