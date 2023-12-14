import os
from flask import Flask, render_template, request, redirect, url_for, flash
from lib.database_connection import get_flask_database_connection

app = Flask(__name__, static_url_path='/static')





if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))