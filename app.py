from flask import Flask, render_template, request, redirect, url_for
from models import db,settings,accounts
from forms import AddZone, LoginForm, RegisterForm
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

		return '<h1>New user has been created!</h1>'
		#return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

	return render_template('signup.html', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
	return render_template('dashboard.html', name=current_user.username)

@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('index'))	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
@app.route('/addZone' ,methods = ['GET' , 'POST'])
def addZone():
	form = AddZone()
	
	if request.method == 'POST':
	#	return "The Zone is: " + form.ZoneName.data #get handle to data....
		settingsObject = settings(form.ZoneName.data,form.BulbID.data)
		
		db.session.add(settingsObject)
		db.session.commit()
		return "success"
	
	
	
	elif request.method == 'GET':
		
		return render_template("AddZone.html" , form = form)

		#return render_template("addZone.html")

	
	
	
	
if __name__ == "__main__":
	app.run(debug=True)