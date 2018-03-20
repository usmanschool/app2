from flask import Flask, render_template, request
from models import db,settingss
from forms import AddZone



app = Flask (__name__)

app.config ['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:ambo123@localhost/amboDB'

app.config['SECRET_KEY'] = 'DontTellAnyOne'
db.init_app(app)




@app.route('/')

def index():
	return render_template("index.html")
	
@app.route('/addZone' ,methods = ['GET' , 'POST'])
def addZone():
	form = AddZone()
	
	if request.method == 'POST':
	#	return "The Zone is: " + form.ZoneName.data #get handle to data....
		settingsObject = settingss(form.ZoneName.data,form.BulbID.data)
		
	
		
		#db.session.add(settingsObject)
		#db.session.commit()
		return "success"
	
	
	
	elif request.method == 'GET':
		
		return render_template("addZone.html" , form = form)

		return render_template("addZone.html")

	
	
	
	
if __name__ == "__main__":
	app.run(debug=True)