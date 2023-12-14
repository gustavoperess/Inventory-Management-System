from lib.product import Product

# Ensure that the user's class is correct

def test_product():
    product = Product(1, "eggs", 3, "dairy")
    assert product.id == 1
    assert product.product_name == "eggs"
    assert product.quantity == 3
    assert product.category == "dairy"

# Ensure that the user's class is formated nicely.

def test_product_formated_nicetly():
    product = Product(1,"eggs", 3, "dairy")
    assert str(product) == "Product(1, eggs, 3, dairy)"