from lib.user import User

class UserRepository:
    def __init__(self, connection):
        self._connection = connection
        self.existing_user = False
        self.existing_email = False
    
    def all(self):
        rows = self._connection.execute('SELECT * from users')
        users = []
        for row in rows:
            user = User(row['id'], row['username'], row['password'], row['email'])
            users.append(user)
        return users
    
        
    def find(self, user_id):
        rows = self._connection.execute(
            'SELECT * from users WHERE id = %s', [user_id])
        
        if rows:
            row = rows[0]
            return User(row['id'], row['username'], row['password'], row['email'])
        else:
            return None
    
        
    def find_name(self, name):
        rows = self._connection.execute(
            'SELECT username FROM users WHERE username = %s', [name]
        )
        
        if rows:
            row = rows[0]
            return row['username'] if row else None
        else:
            return None
    
    def find_email(self, email):
        rows = self._connection.execute(
            'SELECT email FROM users WHERE email = %s', [email]
        )
        
        if rows:
            row = rows[0]
            return row['email'] if row else None
        else:
            return None
        
    
    def create(self, user):
        user_already_exist = self.find_name(user.username)
        email_already_exist = self.find_email(user.email)     
        if user_already_exist == None and email_already_exist == None:
            users = self._connection.execute('INSERT INTO users (username, password, email) VALUES (%s, %s, %s) RETURNING id, username, email', [
                                            user.username, user.password, user.email])
            
            user = users[0]
            return True, user
        else:
            return False, None
      
      
      
      

    
    
