from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, SelectField, DecimalField, IntegerField
from wtforms.validators import InputRequired, Length, ValidationError

category_names = [
            ('FR', 'Fruit'),
            ('VE', 'Vegetable'),
            ('DA', 'Dairy'),
            ('ME', 'Meat'),
            ('SF', 'Seafood'),
            ('BA', 'Bakery'),
            ('BR', 'Breakfast'),
            ('PA', 'Pantry'),
            ('CG', 'Canned Goods'),
            ('PC', 'Personal Care'),
            ('HH', 'Household'),
            ]

class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})
    email = EmailField(validators=[InputRequired(), Length(min=8, max=100)], render_kw={"placeholder": "Email"})
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField('Login')
    
class AddProductForm(FlaskForm):
    product_name = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "ProductName"})
    category = SelectField('Programming Language', choices=category_names)
    quantity = IntegerField('Quantity',validators=[InputRequired()])
    price = DecimalField('Price', places=3, render_kw={"placeholder": "Price"})   
    submit = SubmitField('Add')
    
    
    

