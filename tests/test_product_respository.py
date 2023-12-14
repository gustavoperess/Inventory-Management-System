from lib.product_repository import ProductRepository
from lib.product import Product


"""
When we call ProductRepository#all
We find all products from the database.
"""

def test_find_all_products(db_connection):
    db_connection.seed("seeds/IMG.sql") 
    repository = ProductRepository(db_connection) 
    
    products = repository.all()
    
    assert products == [
        Product(1, 'milk', 5, 'dairy', 1),
        Product(2, 'eggs', 3,  'dairy', 1),
        Product(3, 'lettuce', 1, 'vegetables', 2)
    ]



"""
When we call ProductRepository#find
We find a single product from the database by the ID number.
"""

def test_find_single_product(db_connection):
    db_connection.seed("seeds/IMG.sql")  # Seed our database with some test data
    repository = ProductRepository(db_connection)  # Create a new ArtistRepository

    user = repository.find(1)
    assert user ==  Product(1, 'milk', 5, 'dairy', 1)
    


"""
When we call ProductRepository#create
We create a record from the database.
"""

def test_create_product(db_connection):
    db_connection.seed("seeds/IMG.sql")  # Seed our database with some test data
    repository = ProductRepository(db_connection)  # Create a new ArtistRepository
    
    create_product = repository.create(Product(None, 'tomato', 3, 'fruit', 1))
    assert create_product ==  Product(4, 'tomato', 3, 'fruit', 1)
    
    all_products = repository.all()
    assert  all_products == [
        Product(1, 'milk', 5, 'dairy', 1),
        Product(2, 'eggs', 3,  'dairy', 1),
        Product(3, 'lettuce', 1, 'vegetables', 2),
        Product(4, 'tomato', 3, 'fruit', 1)
    ]
    
def test_to_delete(db_connection):
    db_connection.seed("seeds/IMG.sql") 
    repository = ProductRepository(db_connection) 
   
    assert repository.delete(1) == None
    assert repository.all() == [
        Product(2, 'eggs', 3,  'dairy', 1),
        Product(3, 'lettuce', 1, 'vegetables', 2)
    ]

# # """
# # When we call UserRepository#delete
# # We remove a record from the database.
# # """

# # NEED TO COME BACK TO HANDLE HOW TO DELETE BOTH THE USER IS DELETED 

# # def test_delete_record(db_connection):
# #     db_connection.seed("seeds/users.sql")
# #     repository = UserRepository(db_connection)

# #     assert repository.delete(2) == None
# #     assert repository.all() == [
# #         User(1, 'Gustavo', 'Gustavo123'),
# #         User(3, 'Mario', 'Mario123'),
# #         User(4, 'Rosangela', 'Rosangela123'),
# #     ]