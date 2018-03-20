#add all of the forms here..... (basically collections of data.)


from flask_wtf import Form
from wtforms import StringField, SubmitField

class AddZone(Form):
	ZoneName = StringField('Zone Name')
	BulbID = StringField ('List of Bulb IDs')
	submit = SubmitField ('Create')