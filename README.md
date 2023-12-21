

### Overview

User Authentication: the users can register with a unique username and email. Passwords are securely hashed using bcrypt.
Existing usernames and emails are checked during registration to ensure uniqueness.

Registered users can log in with their credentials. Sessions are managed using Flask-Login. Users can log out to end their sessions.

Users can add, edit, and delete products associated with their accounts. Product information includes name, quantity, category, price, and the date added.
User Dashboard:

After login, users are directed to a dashboard displaying their products. The dashboard includes a filter option to sort products based on different criteria.
Pagination is implemented to display a limited number of products per page.

GPT (Generative Pre-trained Transformer) is integrated to generate prompts based on product names. GPT data is stored in the session during product information retrieval.


### Technologies Used

1. [Flask: A micro web framework for Python.](https://flask.palletsprojects.com/en/2.3.x/)
2. [Flask-Bcrypt: An extension for Flask that provides Bcrypt hashing utilities.](https://flask-bcrypt.readthedocs.io/en/1.0.1/)
3. [Flask-Login: An extension for Flask that manages user sessions.](https://flask-login.readthedocs.io/en/latest/)
4. [Flask-WTF: An integration of the WTForms library with Flask for handling web forms.](https://flask-wtf.readthedocs.io/en/1.2.x/)
5. [Flask-Paginate: An extension for Flask to simplify pagination.](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/pagination/)
6. [PostgreSQL: A relational database management system used to store user and product data.](https://www.postgresql.org/)


###  Setup Prerequisites
```
Instalation

    Python: Ensure you have Python installed on your system.
    PostgreSQL: Install and configure PostgreSQL to serve as the application's database.
    Dependencies: Install project dependencies using pip install -r requirements.txt.

Configuration

    Secret Key: A secret key is set in the application configuration for security purposes.
    Session Lifetime: The session lifetime is set to 30 minutes, and the session refreshes with each request.
    Functionality

Usage

    Execute python app.py to start the Flask development server.
    Access the application at http://127.0.0.1:5001/ in your web browser.
    Interact with the Website:

    Register a new user account or log in with existing credentials.
    Add, edit, and delete products on the user dashboard.
    Explore GPT-generated prompts on the product information pages.
    Logout:

```

