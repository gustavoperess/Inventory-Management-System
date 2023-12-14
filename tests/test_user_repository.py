from lib.user_repository import UserRepository
from lib.user import User


"""
When we call UserRepository#all
We find all users from the database.
"""

def test_all_users(db_connection):
    db_connection.seed("seeds/IMG.sql") 
    repository = UserRepository(db_connection) 
    
    users = repository.all()
    
    assert users == [
        User(1, 'Gustavo', 'gustavo123', 'gustavo123@gmail.com'),
        User(2, 'Ashley', 'ashley123', 'ashley123@gmail.com'),
        User(3, 'Mario', 'mario123', 'mario123@gmail.com'),
        User(4, 'Rosangela', 'rosangela123', 'rosangela123@gmail.com')
    ]
