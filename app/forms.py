from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length

class RegistrationForm(FlaskForm):
	firstname = StringField('firstname') 
	lastname = StringField('lastname')
	usertype = StringField('usertype')
	username = StringField('username', validators=[DataRequired(), Length(min=4,max=20)]) #min4 max 20
	password = PasswordField('password', validators=[DataRequired(), Length(min=6,max=50)]) #min 6 #max 50
	confirm = PasswordField('confirm', validators=[DataRequired(), EqualTo('password', message='Passwords must match.')])

class LoginForm(FlaskForm):
	username = StringField('username')
	password = PasswordField('password')
	rfid = PasswordField('rfid')

class ItemForm(FlaskForm):
    categories = [('Sports', 'Sports'),
                   ('Literary', 'Literary'),
                   ('Cultural', 'Cultural')]
    item_name = StringField('Item')
    statuses = [('Available', 'Available'),
            ('Not Available', 'Not Available')]
    quantity = StringField('Quantity')
    category = SelectField('Category', choices = categories)
    status = SelectField('Status', choices = statuses)
    submit = SubmitField('Submit')


class InvestmentForm(FlaskForm): 
    investment_amount = StringField('Investment Amount')
    submit = SubmitField('Submit')

class HectaresForm(FlaskForm): 
    hectares_total = StringField('Hectares')
    submit = SubmitField('Submit')

class ReforestationForm(FlaskForm): 
    reforestation_total = StringField('Hectares')
    submit = SubmitField('Submit')

class FireControlForm(FlaskForm): 
    firecontrol_item= StringField('Item Name')
    firecontrol_description = StringField('Description')
    firecontrol_qty= StringField('Quantity')
    firecontrol_total= StringField('Total')
    firecontrol_personnel= StringField('Assigned Personnel')
    firecontrol_remarks= StringField('Remarks')
    submit = SubmitField('Submit')