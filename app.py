from flask import Flask, render_template, request, redirect, url_for,session
from models import db,settings,accounts,zonetable
from forms import AddZoneForm, LoginForm, RegisterForm, AdjustBrightnessForm
from flask_bootstrap import Bootstrap
import os
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

app = Flask (__name__)

if os.environ.get('ENV') == 'production':
	app.config ['SQLALCHEMY_DATABASE_URI'] = os.environ.get ('DATABASE_URL')
else:
	app.config ['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:ambo123@localhost/amboDB'

app.config['SECRET_KEY'] = 'DontTellAnyOne'

bootstrap = Bootstrap(app)

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
	return accounts.query.get(int(user_id))



@app.route('/')

def index():
	return render_template("index.html")
	
	
	
@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()

	if form.validate_on_submit():
		user = accounts.query.filter_by(username=form.username.data).first()
		if user:
			if check_password_hash(user.password, form.password.data):
				login_user(user)
				return redirect(url_for('dashboard'))

		return '<h1>Invalid username or password</h1>'
		#return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

	return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	form = RegisterForm()

	if form.validate_on_submit():
		hashed_password = generate_password_hash(form.password.data, method='sha256')
		new_user = accounts(username=form.username.data, password=hashed_password)
		db.session.add(new_user)
		db.session.commit()

		return redirect(url_for('index'))	
		#return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

	return render_template('signup.html', form=form)
	
	
	
@app.route('/addZone', methods = ['GET','POST'])
@login_required
def addZone():
	form = AddZoneForm()
	if form.validate_on_submit():
		newZone = zonetable(uid = current_user.id,zonename = form.ZoneName.data,bulbid = form.BulbID.data,brightnesssetting = 0,lightsensorid = form.LightSensorId.data, overrideflag = 0, energysavingmode = 0, zonebrightnesslowerbound = form.zonebrightnesslowerbound.data, zonebrightnessupperbound = form.zonebrightnessupperbound.data)
		db.session.add(newZone)
		db.session.commit()
		return redirect(url_for('dashboard'))	

	return render_template('additionalzone.html',form = form)


	
@app.route('/modifyZone',methods = ['GET','POST'])
@login_required
def modifyZone():

	form = AddZoneForm()

	#bla bla bla initialize data........
	if 'zoneid' in request.args:
		id = request.args.get('zoneid', None)
		session['curzoneid'] = id
		thezone = zonetable.query.filter_by(zoneid= id).first()
		form.ZoneName.data = thezone.zonename
		form.BulbID.data = thezone.bulbid
		form.LightSensorId.data = thezone.lightsensorid
		form.zonebrightnesslowerbound.data = thezone.zonebrightnesslowerbound
		form.zonebrightnessupperbound.data = thezone.zonebrightnessupperbound

	#when you change it save it.
	if form.validate_on_submit():
		id = session.get('curzoneid', None)
		mazone = zonetable.query.filter_by(zoneid= id).first()
		mazone.zonename = form.ZoneName.data
		mazone.bulbid = form.BulbID.data
		mazone.lightsensorid = form.LightSensorId.data
		mazone.zonebrightnesslowerbound = form.zonebrightnesslowerbound.data
		mazone.zonebrightnessupperbound = form.zonebrightnessupperbound.data
		db.session.commit()
		session.pop('curzoneid')
		return redirect(url_for('dashboard'))	

	return render_template('modifyZone.html',form = form)	
	

	
@app.route('/manualAdjust',methods = ['GET','POST'])
@login_required
def manualAdjust():

	form = AdjustBrightnessForm()

	if 'zoneid' in request.args:
		id = request.args.get('zoneid', None)
		session['curzoneid'] = id
		thezone = zonetable.query.filter_by(zoneid= id).first()
		form.Override.data = thezone.overrideflag
		form.Brightness.data = thezone.brightnesssetting


	#when you change it save it.
	if form.validate_on_submit():
		id = session.get('curzoneid', None)
		mazone = zonetable.query.filter_by(zoneid= id).first()
		mazone.overrideflag = form.Override.data
		mazone.brightnesssetting = form.Brightness.data
		db.session.commit()
		session.pop('curzoneid')
		return redirect(url_for('dashboard'))

	return render_template('manualAdjust.html',form = form)	
	

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
@app.route('/dashboard',methods = ['GET','POST'])
@login_required
def dashboard():
	myzones = zonetable.query.filter_by(uid=current_user.id).all()
	return render_template('dashboard.html', name=current_user.username,myid = current_user.id,zoneList = myzones)


@app.route('/disableAllLights',methods = ['GET','POST'])
@login_required
def disableAllLights():
	print ("disable lights please")
	myzones = zonetable.query.filter_by(uid=current_user.id).all()
	
	for zone in myzones:
		zone.overrideflag = 1;
		zone.brightnesssetting = 0;
	
	db.session.commit()
	return redirect(url_for('dashboard'))
	#return ('', 204)
	
	
	

@app.route('/enableAllLights',methods = ['GET','POST'])
@login_required
def enableAllLights():
	print ("enable lights pelase")
	myzones = zonetable.query.filter_by(uid=current_user.id).all()
	for zone in myzones:
		zone.overrideflag = 0;
		zone.brightnesssetting = 10;

	db.session.commit()
	return redirect(url_for('dashboard'))
	#return ('', 204	)
	
	
	
	
@app.route('/energySavingModeOn',methods = ['GET','POST'])
@login_required
def energySavingModeOn():
	print ("energy saving mode please")
	myzones = zonetable.query.filter_by(uid=current_user.id).all()
	
	for zone in myzones:
		zone.energysavingmode = 1;
	
	db.session.commit()
	return redirect(url_for('dashboard'))

	
	#return ('', 204)
		

@app.route('/energySavingModeOff',methods = ['GET','POST'])
@login_required
def energySavingModeOff():
	print ("energy saving mode off please")
	myzones = zonetable.query.filter_by(uid=current_user.id).all()
		
	for zone in myzones:
		zone.energysavingmode = 0;
	
	db.session.commit()
	return redirect(url_for('dashboard'))

	#return ('', 204)


@app.route('/deleteZone',methods = ['GET','POST'])
@login_required
def deleteZone():
	id = request.args.get('zoneid', None)
	zonetable.query.filter_by(zoneid=id).delete()
	db.session.commit()
	return redirect(url_for('dashboard'))


	

@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('index'))	
	
	

	

	


	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
if __name__ == "__main__":
	app.run(debug=True)