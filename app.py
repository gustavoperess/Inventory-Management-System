import os
from flask import Flask, render_template, request, redirect, url_for, flash
from lib.database_connection import get_flask_database_connection
from lib.user_repository import UserRepository
from lib.product_repository import ProductRepository
from lib.product import Product
from flask_login import login_user, LoginManager, login_required, logout_user, current_user
from lib.user import User
from lib.forms import LoginForm, RegisterForm, AddProductForm, Filters
from flask_bcrypt import Bcrypt
from flask_paginate import Pagination, get_page_args
from lib.api import API_KEY
from datetime import date

app = Flask(__name__, static_url_path='/static')
bcrypt = Bcrypt(app)
app.config['SECRET_KEY'] = API_KEY().database


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login_page"


@login_manager.user_loader
def load_user(user_id):
    connection = get_flask_database_connection(app)
    
    # Load user information
    user_repository = UserRepository(connection)
    user = user_repository.find(int(user_id))
    
    # Load products information
    product_repository = ProductRepository(connection)
    products = product_repository.find(int(user_id))

    if user:
        user.products = products
    
    return user


@app.route('/', methods=['GET', 'POST'])
def main_page():
    form = LoginForm()
    if form.validate_on_submit():
        connection = get_flask_database_connection(app)
        repository = UserRepository(connection)
        user = repository.find_by_name(form.username.data)
        if user is None:
            flash("User not in the system")
        
        elif not bcrypt.check_password_hash(user.password.encode('utf-8'), form.password.data.encode('utf-8')):
            flash("Password is incorrect")
        
        elif user and bcrypt.check_password_hash(user.password.encode('utf-8'), form.password.data.encode('utf-8')):   
                login_user(user)      
                return redirect(url_for('login_page'))
            
    return render_template('index.html', form=form)




@app.route('/product_information', methods=['GET', 'POST'])
def product_information():
    pass


@app.route('/login', methods=['GET', 'POST'])
@login_required
def login_page():
    connection = get_flask_database_connection(app)
    product_repository = ProductRepository(connection)
    user_repository = UserRepository(connection)
    
    all_users = user_repository.all()
    product_count = product_repository.product_count(current_user.id)
    
    form = Filters()
    filter_by_products = None
    if filter_by_products is None:
        default_filter = "First Added" 
        filter_by_products = product_repository.filter_by(default_filter)
    
    if form.validate_on_submit():
        selected_filter = form.selected_filter.data
        filter_by_products = product_repository.filter_by(selected_filter)
        

    if request.method == 'POST' and 'delete_post' in request.form:
        product_id_to_delete = int(request.form['delete_post'])
        product_repository.delete(product_id_to_delete)
        return redirect(url_for('login_page'))
    
    if request.method == 'POST' and 'update_post' in request.form:
        
        # product_to_update = int(request.form['update_post'])
        # product_name=request.form['product_name'],
        # quantity=int(request.form['quantity']),
        # category=request.form['category'],
        # price=float(request.form['price']),
        # today = date.today()
        # update_product = Product(product_to_update, product_name,quantity, category, price, today,  current_user.id)
        # product_repository.update(update_product)
        return render_template(('product_information.html'))
    
    
    page, per_page, offset= get_page_args()
    total = len(filter_by_products)
    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')
    paginated_products = filter_by_products[offset: offset + per_page]

    
    return render_template('login.html', user=current_user, all_users=all_users,
                           product_count=product_count, form=form,
                           filter_by_products=paginated_products, pagination=pagination)
    


@app.route('/add_item', methods=['GET', 'POST'])
@login_required
def add_item():
    add_form = AddProductForm()
    if add_form.validate_on_submit():
        today = date.today()
        connection = get_flask_database_connection(app)
        product = ProductRepository(connection)
        new_product = Product(None, add_form.product_name.data, add_form.quantity.data, add_form.category.data, add_form.price.data , today , current_user.id)
        product.create(new_product)
    return render_template('add_item.html', form=add_form)



@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('main_page'))



@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():       
        connection = get_flask_database_connection(app)
        repository = UserRepository(connection)
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User(None, username=form.username.data, password=hashed_password, email=form.email.data)
        success, user = repository.create(new_user)
        if success:
            flash("Registration successful")
            return redirect(url_for('main_page'))
        
        elif not success and repository.find_name(form.username.data) is not None and not success and repository.find_email(form.email.data) is not None:
            flash("Username and email already exist. Please choose a different username and email.")
        
        elif not success and repository.find_name(form.username.data) is not None:
            flash("Username already exists. Please choose a different username.")
        elif not success and repository.find_email(form.email.data) is not None:
            flash("Email already exists. Please choose a different email.")

      
    return render_template('register.html', form=form)
    
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))


