from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, SelectField, DecimalField, IntegerField
from wtforms.validators import InputRequired, Length, ValidationError


category_names = [
        ('Household', 'Household'),
        ('Fruit', 'Fruit'),
        ('Vegetable', 'Vegetable'),
        ('Dairy', 'Dairy'),
        ('Meat', 'Meat'),
        ('Seafood', 'Seafood'),
        ('Bakery', 'Bakery'),
        ('Breakfast', 'Breakfast'),
        ('Pantry', 'Pantry'),
        ('Canned Goods', 'Canned Goods'),
        ('Personal Care', 'Personal Care'),
    ]


dropdowchoises = [
        ('First Added', 'First Added'),
        ('Last Added', 'Last Added'),
        ('Price: Low to High', 'Price: Low to High'),
        ('Price: High to Low', 'Price: High to Low'),
        ('Category', 'Category'),
        ('Name', 'Name'),
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
    product_name = StringField(validators=[InputRequired(), Length(min=0, max=20)], render_kw={"placeholder": "ProductName"})
    quantity = IntegerField(validators=[InputRequired()], render_kw={"placeholder": "Quanity"})
    price = DecimalField(validators=[InputRequired()], places=2, render_kw={"placeholder": "Price"})
    category = SelectField('Grocery Products', choices=category_names)
    submit = SubmitField('Add')
    
class Filters(FlaskForm):
    selected_filter = SelectField('Sort by:', choices=dropdowchoises)


