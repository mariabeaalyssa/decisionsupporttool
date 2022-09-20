from locale import currency
from app import *
from app import server
from app.forms import *
from app.models import *
from flask import render_template, request, redirect, url_for, flash, session
from flask_login import LoginManager, current_user, login_user, login_required, logout_user
from .models import *
from .forms import *
from werkzeug.security import generate_password_hash, check_password_hash



login_manager = LoginManager()
login_manager.init_app(server)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(id):
	return User.query.get(id)


@server.route('/', methods=["GET","POST"])
def index():
	form = LoginForm()
	return redirect(url_for('login', form=form))

@server.route('/login', methods=["GET","POST"])
def login():
	form = LoginForm()
	if current_user.is_authenticated is True:
		return redirect(url_for('dashboard'))
	elif form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user:
			print(form.password.data)
			if check_password_hash(user.password, form.password.data):
				login_user(user, remember=True)
				session['username'] = request.form['username']
				return redirect(url_for('dashboard'))
			else:
				flash('Invalid username or password')
				return render_template('login.html', form=form)
		else:
			return redirect(url_for('dashboard'))
	return render_template('login.html', form=form)


@server.route('/register', methods=["GET", "POST"])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		new_user = User(form.firstname.data, form.lastname.data, form.usertype.data, form.username.data, form.password.data)
		dbase.session.add(new_user)
		dbase.session.commit()
		
		return redirect(url_for('login'))
	return render_template('register.html', title="Register Admin", form=form)

@server.route('/dashboard', methods=["GET","POST"])
@login_required
def dashboard():
	user = User.query.filter_by(id=current_user.id).first()
	investment = Investment.query.filter_by(investment_id=1).first()
	hectares = Hectares.query.filter_by(hectares_id=1).first()
	reforestation = Reforestation.query.filter_by(reforestation_id=1).first()
	firecontrol = FireControl.query.all()
	form = InvestmentForm()
	form2 = HectaresForm()
	form3 = ReforestationForm()
	form4 = FireControlForm()
	return render_template('index.html', form=form, form2=form2, form3=form3, form4=form4, firecontrol=firecontrol, reforestation=reforestation, hectares=hectares, investment=investment, user=user )

@server.route('/investment',methods=["GET","POST"])
def investment():
    form = InvestmentForm()
    #investment=Investment.query.filter_by(investment_id=1).first()
    if form.validate_on_submit():
        add_investment = Investment(form.investment_amount.data)
        dbase.session.add(add_investment)
        dbase.session.commit()
        return redirect(url_for('dashboard',form=form, investment=investment))
    return redirect(url_for('dashboard',form=form, investment=investment))

@server.route('/update/<int:investment_id>/investment', methods=['GET','POST'])
def update_investment(investment_id):
	form = InvestmentForm()
	investment = Investment.query.get_or_404(investment_id)
	if form.validate_on_submit():
		investment.investment_amount = form.investment_amount.data
		dbase.session.commit()
		flash('Your post has been updated!', 'success')
		return redirect(url_for('dashboard', investment=investment))
	elif request.method == 'GET':
		form.investment_amount.data = investment.investment_amount
		#return numberFormat("Php {:,.2f}".format(investment.investment_amount))
	return redirect(url_for('index.html', form=form, investment=investment))


@server.route('/update/<int:hectares_id>/hectares', methods=['GET','POST'])
def update_hectares(hectares_id):
	form2 = HectaresForm()
	hectares = Hectares.query.get_or_404(hectares_id)
	if form2.validate_on_submit():
		hectares.hectares_total = form2.hectares_total.data
		dbase.session.commit()
		flash('Your post has been updated!', 'success')
		return redirect(url_for('dashboard', hectares=hectares))
	elif request.method == 'GET':
		form2.hectares_total.data = hectares.hectares_total
	return redirect(url_for('index.html', form2=form2, hectares=hectares))


@server.route('/update/<int:reforestation_id>/reforestation', methods=['GET','POST'])
def update_reforestation(reforestation_id):
	form3 = ReforestationForm()
	reforestation = Reforestation.query.get_or_404(reforestation_id)
	if form3.validate_on_submit():
		reforestation.reforestation_total = form3.reforestation_total.data
		dbase.session.commit()
		flash('Your post has been updated!', 'success')
		return redirect(url_for('dashboard', reforestation=reforestation))
	elif request.method == 'GET':
		form3.reforest_total.data = reforestation.reforestation_total
	return redirect(url_for('index.html', form3=form3, reforestation=reforestation))

@server.route('/firecontrol', methods=['GET','POST'])
def add_firecontrol():
	form4 = FireControlForm()
	if form4.validate_on_submit():
		new_firecontrol = FireControl(form4.firecontrol_item.data, form4.firecontrol_description.data, form4.firecontrol_qty.data, form4.firecontrol_total.data, form4.firecontrol_personnel.data, form4.firecontrol_remarks.data)
		dbase.session.add(new_firecontrol)
		dbase.session.commit()
		
		return redirect(url_for('dashboard',form4=form4))
	return render_template('index.html', form4=form4)


@server.route('/rainforestation', methods=['GET','POST'])
def rainforestation():
	form4 = FireControlForm()
	if form4.validate_on_submit():
		new_firecontrol = FireControl(form4.firecontrol_item.data, form4.firecontrol_description.data, form4.firecontrol_qty.data, form4.firecontrol_total.data, form4.firecontrol_personnel.data, form4.firecontrol_remarks.data)
		dbase.session.add(new_firecontrol)
		dbase.session.commit()
		
		return redirect(url_for('dashboard',form4=form4))
	return render_template('index.html', form4=form4)



@server.route('/landcover', methods=['GET','POST'])
def landcover():
	user = User.query.filter_by(id=current_user.id).first()
	investment = Investment.query.filter_by(investment_id=1).first()
	hectares = Hectares.query.filter_by(hectares_id=1).first()
	reforestation = Reforestation.query.filter_by(reforestation_id=1).first()
	firecontrol = FireControl.query.all()
	form = InvestmentForm()
	form2 = HectaresForm()
	form3 = ReforestationForm()
	form4 = FireControlForm()
	return render_template('landcover.html', form=form, form2=form2, form3=form3, form4=form4, firecontrol=firecontrol, reforestation=reforestation, hectares=hectares, investment=investment, user=user )
	


@server.route('/rainscenario', methods=['GET','POST'])
def rainscenario():
	user = User.query.filter_by(id=current_user.id).first()
	investment = Investment.query.filter_by(investment_id=1).first()
	hectares = Hectares.query.filter_by(hectares_id=1).first()
	reforestation = Reforestation.query.filter_by(reforestation_id=1).first()
	firecontrol = FireControl.query.all()
	form = InvestmentForm()
	form2 = HectaresForm()
	form3 = ReforestationForm()
	form4 = FireControlForm()
	return render_template('page_tester.html', form=form, form2=form2, form3=form3, form4=form4, firecontrol=firecontrol, reforestation=reforestation, hectares=hectares, investment=investment, user=user )



@server.route('/logout')
@login_required
def logout():
	session.clear()
	logout_user()
	return redirect(url_for('login'))
	

