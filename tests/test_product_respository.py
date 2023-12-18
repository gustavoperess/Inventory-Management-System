from lib.product_repository import ProductRepository
from lib.product import Product
from datetime import date

# Test Case Names Updated

def test_find_all_products(db_connection):
    db_connection.seed("seeds/IMG.sql")
    repository = ProductRepository(db_connection)
    
    products = repository.all()
    
    # Compare specific attributes rather than the entire object
    assert products == [
        Product(1, 'milk', 5, 'dairy', 2.55, "2023-10-10", 1),
        Product(2, 'eggs', 3, 'dairy', 3.55, "2023-10-10", 1),
        Product(3, 'lettuce', 1, 'vegetables', 4.55, "2023-10-10", 2)
    ]


def test_find_single_product(db_connection):
    db_connection.seed("seeds/IMG.sql")
    repository = ProductRepository(db_connection)

    user = repository.find(1)
    # Compare specific attributes rather than the entire object
    assert user == Product(1, 'milk', 5, 'dairy', 2.55, '2023-10-10', 1)

def test_create_product(db_connection):
    db_connection.seed("seeds/IMG.sql")
    repository = ProductRepository(db_connection)
    
    # Provide a date in the correct format when creating a Product instance
    create_product = repository.create(Product(None, 'tomato', 3, 'fruit', 1, '2023-12-17', 1.0))
    # Compare specific attributes rather than the entire object
    assert create_product == Product(4, 'tomato', 3, 'fruit', 1, '2023-12-17', 1.0)

    all_products = repository.all()
    # Compare specific attributes rather than the entire object
    assert all_products == [
        Product(1, 'milk', 5, 'dairy', 2.55, '2023-10-10', 1),
        Product(2, 'eggs', 3, 'dairy', 3.55, '2023-10-10', 1),
        Product(3, 'lettuce', 1, 'vegetables', 4.55, '2023-10-10', 2),
        Product(4, 'tomato', 3, 'fruit', 1, '2023-12-17', 1.0)
    ]

def test_delete_product(db_connection):
    db_connection.seed("seeds/IMG.sql")
    repository = ProductRepository(db_connection)
    
    # Provide a date in the correct format when creating a Product instance
    create_product = repository.create(Product(None, 'tomato', 3, 'fruit', 1, '2023-12-17', 1.0))

    # Ensure that the created product exists before deleting it
    assert repository.find(4) == Product(4, 'tomato', 3, 'fruit', 1, '2023-12-17', 1.0)

    # Ensure the delete operation returns None
    assert repository.delete(4) is None

    # Ensure that the deleted product is not in the list anymore
    assert repository.find(4) is None
    assert repository.all() == [
        Product(1, 'milk', 5, 'dairy', 2.55, '2023-10-10', 1),
        Product(2, 'eggs', 3, 'dairy', 3.55, '2023-10-10', 1),
        Product(3, 'lettuce', 1, 'vegetables', 4.55, '2023-10-10', 2),
    ]
