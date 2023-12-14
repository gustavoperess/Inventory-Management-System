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
    
    def find_by_name(self, username):
        rows = self._connection.execute(
            'SELECT * from users WHERE username = %s', [username])
         
        if rows:
            row = rows[0]
            return User(row['id'], row['username'], row['password'], row['email'])
        else:
            return None
    
    def find_by_email(self, email):
        rows = self._connection.execute(
            'SELECT * from users WHERE email = %s', [email])
         
        if rows:
            row = rows[0]
            return User(row['id'], row['username'], row['password'], row['email'])
        else:
            return None
    
    
    def create(self, user):
        user_already_exist = self.find_by_name(user.username)
        email_already_exist = self.find_by_email(user.email)
        if not user_already_exist or not email_already_exist:
            rows = self._connection.execute('INSERT INTO users (username, password, email) VALUES (%s, %s, %s) RETURNING id', [
                                            user.username, user.password, user.email])
            
            row = rows[0]
            user.id = self._generate_next_id()
            user.id = row["id"]
            return True, user 
        else:
            return False, None 
    
    # ensure that the nex id always the +1 from the latest created.     
    def _generate_next_id(self):
        users = self.all()
        return max([user.id for user in users], default=0) + 1