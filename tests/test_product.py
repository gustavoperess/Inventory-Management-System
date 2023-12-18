from lib.product import Product

# Ensure that the user's class is correct

def test_product():
    product = Product(1, "eggs", 3, "dairy", 5, "2023-10-10",  1)
    assert product.id == 1
    assert product.product_name == "eggs"
    assert product.quantity == 3
    assert product.category == "dairy"
    assert product.price == 5
    assert product.date_added == '2023-10-10'
    assert product.user_id == 1


# Ensure that the user's class is formated nicely.

def test_product_formated_nicetly():
    product = Product(1, "eggs", 3, "dairy", 5, "2023-10-10", 1)
    assert str(product) == "Product(1, eggs, 3, dairy, 5, 2023-10-10, 1)"
    
    
    
