# Import the User class from the "lib.user" module
from lib.user import User

# Define a class representing a repository for managing user information
class UserRepository:
    # Constructor method that initializes the repository with a database connection
    def __init__(self, connection):
        self._connection = connection
        # Flags to track the existence of a user or email during operations
        self.existing_user = False
        self.existing_email = False
    
    # Retrieve all users from the database and return them as a list of User objects
    def all(self):
        rows = self._connection.execute('SELECT * from users')
        users = []
        for row in rows:
            # Create a User object for each row and append it to the list
            user = User(row['id'], row['username'], row['password'], row['email'])
            users.append(user)
        return users
    
    # Find and return a user based on their ID
    def find(self, user_id):
        rows = self._connection.execute('SELECT * from users WHERE id = %s', [user_id])
        
        # Check if rows are not empty and create a User object
        if rows:
            row = rows[0]
            return User(row['id'], row['username'], row['password'], row['email'])
        else:
            # Return None if the user is not found
            return None
    
    # Find and return a user based on their username
    def find_by_name(self, username):
        rows = self._connection.execute('SELECT * from users WHERE username = %s', [username])
         
        # Check if rows are not empty and create a User object
        if rows:
            row = rows[0]
            return User(row['id'], row['username'], row['password'], row['email'])
        else:
            # Return None if the user is not found
            return None
    
    # Find and return a user based on their email
    def find_by_email(self, email):
        rows = self._connection.execute('SELECT * from users WHERE email = %s', [email])
         
        # Check if rows are not empty and create a User object
        if rows:
            row = rows[0]
            return User(row['id'], row['username'], row['password'], row['email'])
        else:
            # Return None if the user is not found
            return None
    
    # Check if a username exists in the database
    def find_name(self, name):
        rows = self._connection.execute('SELECT username FROM users WHERE username = %s', [name])
        
        # Check if rows are not empty and return the username if found, otherwise return None
        if rows:
            row = rows[0]
            return row['username'] if row else None
        else:
            return None
    
    # Check if an email exists in the database
    def find_email(self, email):
        rows = self._connection.execute('SELECT email FROM users WHERE email = %s', [email])
        
        # Check if rows are not empty and return the email if found, otherwise return None
        if rows:
            row = rows[0]
            return row['email'] if row else None
        else:
            return None
    
    # Create a new user in the database, checking for existing username and email
    def create(self, user):
        # Check if the username and email already exist
        user_already_exist = self.find_name(user.username)
        email_already_exist = self.find_by_email(user.email)     
        if user_already_exist is None and email_already_exist is None:
            # Insert the new user into the database and return success along with the user information
            users = self._connection.execute('INSERT INTO users (username, password, email) VALUES (%s, %s, %s) RETURNING id, username, email', [
                                            user.username, user.password, user.email])
            
            user = users[0]
            return True, user
        else:
            # Return failure if the username or email already exists
            return False, None
