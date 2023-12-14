import os
from flask import Flask, render_template, request, redirect, url_for, flash
from lib.database_connection import get_flask_database_connection
from lib.user_repository import UserRepository
# from lib.products_repository import ProductsRepository
# from lib.products import Products
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

@app.route('/', methods=['GET', 'POST'])
def main_page():
    form = LoginForm()
    if form.validate_on_submit():
        connection = get_flask_database_connection(app)
        repository = UserRepository(connection)
        user = repository.find_by_name(form.username.data)
        if user and bcrypt.check_password_hash(user.username.encode('utf-8'), form.password.data.encode('utf-8')):
                login_user(user)      
                return redirect(url_for('login_page'))
        else:
            flash("User not in the system")
    return render_template('index.html', form=form)
    
    
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
    