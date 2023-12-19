# Import the Product class from the "lib.product" module
from lib.product import Product

# Define a class representing a repository for managing products
class ProductRepository:
    # Constructor method that initializes the repository with a database connection
    def __init__(self, connection):
        self._connection = connection
    
    # Retrieve all products from the database and return them as a list of Product objects
    def all(self):
        rows = self._connection.execute('SELECT * from products')
        products = []
        for row in rows:
            # Create a Product object for each row and append it to the list
            product = Product(row['id'], row['product_name'], row['quantity'], row['category'], row['price'], row['date_added'], row['user_id'])
            products.append(product)
        return products
    
     # Filter  products from the database and return them in order ASC or DESC 
    def filter_by(self, filter):
        products = []
        if filter == "Price: High to Low":
            rows = self._connection.execute('SELECT * from products ORDER BY price DESC')
            for row in rows:
                product = Product(row['id'], row['product_name'], row['quantity'], row['category'], row['price'], row['date_added'], row['user_id'])
                products.append(product)
        elif filter == "Price: Low to High":
            rows = self._connection.execute('SELECT * from products ORDER BY price ASC')
            for row in rows:
                product = Product(row['id'], row['product_name'], row['quantity'], row['category'], row['price'], row['date_added'], row['user_id'])
                products.append(product)
        elif filter == "Category":
            rows = self._connection.execute('SELECT * from products ORDER BY category ASC')
            for row in rows:
                product = Product(row['id'], row['product_name'], row['quantity'], row['category'], row['price'], row['date_added'], row['user_id'])
                products.append(product)
        elif filter == "Name":
            rows = self._connection.execute('SELECT * from products ORDER BY product_name ASC')
            for row in rows:
                product = Product(row['id'], row['product_name'], row['quantity'], row['category'], row['price'], row['date_added'], row['user_id'])
                products.append(product)
        elif filter == "First Added":
            rows = self._connection.execute('SELECT * from products ORDER BY id ASC')
            for row in rows:
                product = Product(row['id'], row['product_name'], row['quantity'], row['category'], row['price'], row['date_added'], row['user_id'])
                products.append(product)
        elif filter == "Last Added":
            rows = self._connection.execute('SELECT * from products ORDER BY id DESC')
            for row in rows:
                product = Product(row['id'], row['product_name'], row['quantity'], row['category'], row['price'], row['date_added'], row['user_id'])
                products.append(product)
     
        return products
                
    # Calculate and return aggregated information about the products for a specific user
    def product_count(self, current_user):
        rows = self._connection.execute('SELECT * from products')
        products = []
        for row in rows:
            # Create a Product object for each row and append it to the list
            product = Product(row['id'], row['product_name'], row['quantity'], row['category'], row['price'], row['date_added'], row['user_id'])
            products.append(product)
        
        # Initialize a dictionary to store aggregated information
        result = {}
        
        # Iterate through each product and aggregate information based on user and category
        for product in products:
            if current_user == product.user_id:
                category = product.category
                price = product.price 
                user_id = product.user_id
                total_quantity = product.quantity
        
                # Update the result dictionary with aggregated information
                if category in result:
                    result[category]['quantity'] += int(total_quantity)
                    result[category]['category_count'] += 1
                    result[category]['price'] += price 
                    result[category]['user_id'] = user_id
                else:
                    result[category] = {'category_count': 1, 'price': price, 'user_id': user_id, 'quantity': total_quantity}
      
        # Return the aggregated information
        return result
        
    # Find and return a product based on its ID
    def find(self, product_id):
        rows = self._connection.execute('SELECT * from products WHERE id = %s', [product_id])
        
        # Check if rows are not empty and create a Product object
        if rows:
            row = rows[0]
            return Product(row['id'], row['product_name'], row['quantity'], row['category'], row['price'], row['date_added'], row['user_id'])
        else:
            # Return None if the product is not found
            return None

    # Insert a new product into the database and return the updated Product object with the assigned ID
    def create(self, product):
        rows = self._connection.execute('INSERT INTO products (product_name, quantity, category, price, date_added, user_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id', [
                                        product.product_name, product.quantity, product.category, product.price, product.date_added, product.user_id])
        
        # Get the assigned ID for the newly created product
        row = rows[0]
        product.id = self._generate_next_id()
        product.id = row["id"]
        return product 

    # Delete a product from the database based on its ID
    def delete(self, id):
        self._connection.execute("DELETE FROM products WHERE id = %s", [id])
        # Return None after deleting the product
    
        
    def update(self, product):
        self._connection.execute(
            "UPDATE products SET product_name = %s, quantity = %s, category = %s, price = %s WHERE id = %s",
            [product.product_name, product.quantity, product.category, product.price, product.id]
        )
    
    
    # Ensure that the next ID is always one greater than the latest created product's ID     
    def _generate_next_id(self):
        # Retrieve all products and calculate the next available ID
        users = self.all()
        return max([user.id for user in users], default=0) + 1
