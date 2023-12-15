import os
from flask import Flask, render_template, request, redirect, url_for, flash
from lib.database_connection import get_flask_database_connection
from lib.user_repository import UserRepository
from lib.product_repository import ProductRepository
from lib.product import Product
from flask_login import login_user, LoginManager, login_required, logout_user, current_user
from lib.user import User
from lib.forms import LoginForm, RegisterForm
from flask_bcrypt import Bcrypt
from datetime import datetime

app = Flask(__name__, static_url_path='/static')
bcrypt = Bcrypt(app)
app.config['SECRET_KEY'] = 'thisisasecretkey'


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
        if user and bcrypt.check_password_hash(user.password.encode('utf-8'), form.password.data.encode('utf-8')):   
                login_user(user)      
                return redirect(url_for('login_page'))
        else:
            flash("User not in the system")
    return render_template('index.html', form=form)




@app.route('/login', methods=['GET', 'POST'])
@login_required
def login_page():
    connection = get_flask_database_connection(app)
    product_repository = ProductRepository(connection)
    user_repository = UserRepository(connection)
    
    all = product_repository.all()
    all_users = user_repository.all()
    
    if not current_user.products:
        flash("User does not have any posts yet")

    if request.method == 'POST' and 'delete_post' in request.form:
        product_id_to_delete = int(request.form['delete_post'])
        connection = get_flask_database_connection(app)
        new_repo = ProductRepository(connection)
        new_repo.delete(product_id_to_delete)
        
        return redirect(url_for('login_page'))
               
    return render_template('login.html', user=current_user, all=all, all_users=all_users)
    


@app.route('/add_item', methods=['GET', 'POST'])
@login_required
def add_item():
    connection = get_flask_database_connection(app)
    product = ProductRepository(connection)
    
    if request.method == "POST":
        product_name = request.form['name']
        quantity = request.form['quantity']
        category = request.form['category']
        new_product = Product(None, product_name, quantity, category, current_user.id)
        product.create(new_product)
        
        return redirect(url_for('login_page'))
    
    return render_template('add_item.html')



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
    