from lib.user import User

# Ensure that the user's class is correct

def test_user():
    user = User(1, "gustavoperess", "gustavoperes123", "gustavoperess123@gmail.com")
    assert user.id == 1
    assert user.username == "gustavoperess"
    assert user.password == "gustavoperes123"
    assert user.email == "gustavoperess123@gmail.com"

# Ensure that the user's class is formated nicely.

def test_user_formated_nicetly():
    user = User(1,"gustavoperess","gustavoperes123", "gustavoperess123@gmail.com")
    assert str(user) == "User(1, gustavoperess, gustavoperes123, gustavoperess123@gmail.com)"