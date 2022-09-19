from app import dbase, generate_password_hash, UserMixin

class User(UserMixin, dbase.Model):
	
	__tablename__ = 'user'
    
	id = dbase.Column(dbase.Integer, primary_key=True)
	firstname = dbase.Column(dbase.String(50), nullable=False)
	lastname = dbase.Column(dbase.String(50), nullable=False)
	usertype = dbase.Column(dbase.String(50), nullable=False)
	username = dbase.Column(dbase.String(50), nullable=False)
	password = dbase.Column(dbase.String(200), nullable=False)
	
	
	def __init__(self, firstname='',lastname='', usertype='', username='', password=''):
		self.firstname = firstname
		self.lastname = lastname
		self.usertype = usertype
		self.username = username
		self.password = generate_password_hash(password, method='sha256')
		
class Item(dbase.Model):
    __tablename__ = "items"

    item_id = dbase.Column(dbase.Integer, primary_key=True)
    item_name = dbase.Column(dbase.String(50))
    category = dbase.Column(dbase.String(50))
    quantity = dbase.Column(dbase.Integer)
    total = dbase.Column(dbase.Integer)


    def __init__(self, item_name='',category='', quantity='', total=''):
        self.item_name = item_name
        self.category = category
        self.quantity = quantity
        self.total = total

class Investment(dbase.Model):
	__tablename__="investments"

	investment_id = dbase.Column(dbase.Integer, primary_key=True)
	investment_amount = dbase.Column(dbase.Float)

	def __init__(self, investment_amount=''):
		self.investment_amount = investment_amount

class Hectares(dbase.Model):
	__tablename__="hectares"

	hectares_id = dbase.Column(dbase.Integer, primary_key=True)
	hectares_total = dbase.Column(dbase.Integer)

	def __init__(self, hectares_total=''):
		self.hectares_total = hectares_total

class Reforestation(dbase.Model):
	__tablename__="reforestation"

	reforestation_id = dbase.Column(dbase.Integer, primary_key=True)
	reforestation_total = dbase.Column(dbase.Integer)

	def __init__(self, reforestation_total=''):
		self.reforestation_total = reforestation_total

class FireControl(dbase.Model):
	__tablename__="firecontrol"

	firecontrol_id = dbase.Column(dbase.Integer, primary_key=True)
	firecontrol_item = dbase.Column(dbase.String(200))
	firecontrol_description = dbase.Column(dbase.String(200))
	firecontrol_qty = dbase.Column(dbase.Integer)
	firecontrol_total = dbase.Column(dbase.Integer)
	firecontrol_personnel = dbase.Column(dbase.String(200))
	firecontrol_remarks = dbase.Column(dbase.String(200))

	def __init__(self, firecontrol_item='', firecontrol_description ='', firecontrol_qty='', firecontrol_total='', firecontrol_personnel='', firecontrol_remarks=''):
		self.firecontrol_item = firecontrol_item
		self.firecontrol_description = firecontrol_description
		self.firecontrol_qty = firecontrol_qty
		self.firecontrol_total = firecontrol_total
		self.firecontrol_personnel = firecontrol_personnel
		self.firecontrol_remarks = firecontrol_remarks