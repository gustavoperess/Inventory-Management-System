import os
from flask import Flask, render_template, request, redirect, url_for, flash
from lib.database_connection import get_flask_database_connection
from lib.user_repository import UserRepository
# from lib.post_repository import PostRepository
# from lib.post import Post
from flask_login import login_user, LoginManager, login_required, logout_user, current_user
from lib.user import User
# from lib.forms import LoginForm, RegisterForm
from flask_bcrypt import Bcrypt
from datetime import datetime

app = Flask(__name__, static_url_path='/static')
bcrypt = Bcrypt(app)
app.config['SECRET_KEY'] = 'thisisasecretkey'


@app.route('/', methods=['GET', 'POST'])
def main_page():
    return render_template('index.html')
    
    
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))