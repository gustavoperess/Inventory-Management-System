# Inventory-Management-System
An example of a Inventory Management System



Overview
This Flask application is a simple web platform for managing user accounts and product information. Users can register, log in, add, edit, and delete products associated with their accounts.

Technologies Used
Flask: A micro web framework for Python.
Flask-Bcrypt: An extension for Flask that provides Bcrypt hashing utilities.
Flask-Login: An extension for Flask that manages user sessions.
Flask-WTF: An integration of the WTForms library with Flask for handling web forms.
Flask-Paginate: An extension for Flask to simplify pagination.
PostgreSQL: A relational database management system used to store user and product data.

# Setup Prerequisites
```
Instalation

    Python: Ensure you have Python installed on your system.
    PostgreSQL: Install and configure PostgreSQL to serve as the application's database.
    Dependencies: Install project dependencies using pip install -r requirements.txt.

Configuration

    Secret Key: A secret key is set in the application configuration for security purposes.
    Session Lifetime: The session lifetime is set to 30 minutes, and the session refreshes with each request.
    Functionality

```

User Authentication:
Users can register with a unique username and email.
Passwords are securely hashed using bcrypt.
Existing usernames and emails are checked during registration to ensure uniqueness.
User Login and Logout:

Registered users can log in with their credentials.
Sessions are managed using Flask-Login.
Users can log out to end their sessions.
Product Management:

Users can add, edit, and delete products associated with their accounts.
Product information includes name, quantity, category, price, and the date added.
User Dashboard:

After login, users are directed to a dashboard displaying their products.
The dashboard includes a filter option to sort products based on different criteria.
Pagination is implemented to display a limited number of products per page.
GPT Integration:

GPT (Generative Pre-trained Transformer) is integrated to generate prompts based on product names.
GPT data is stored in the session during product information retrieval.
Usage
Run the Application:

Execute python app.py to start the Flask development server.
Access the application at http://127.0.0.1:5001/ in your web browser.
Interact with the Website:

Register a new user account or log in with existing credentials.
Add, edit, and delete products on the user dashboard.
Explore GPT-generated prompts on the product information pages.
Logout:

Click the logout option to end the current session.
