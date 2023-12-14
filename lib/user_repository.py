from lib.user import User

class UserRepository:
    def __init__(self, connection):
        self.connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * from users')
        users = []
        for row in rows:
            user = User(row['id'], row['username'], row['password'], row['email'])
            users.append(user)
        return users
        
