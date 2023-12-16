from lib.product import Product

class ProductRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * from products')
        products = []
        for row in rows:
            product = Product(row['id'], row['product_name'], row['quantity'], row['category'], row['price'], row['user_id'])
            products.append(product)
        return products
    
    def product_count(self):
        rows = self._connection.execute('SELECT * from products')
        products = []
        for row in rows:
            product = Product(row['id'], row['product_name'], row['quantity'], row['category'], row['price'], row['user_id'])
            products.append(product)
        
        result = {}

        for product in products:
            category = product.category
            price = product.price

            if category in result:
                result[category]['category_count'] += 1
                result[category]['price'] += price

            else:
                result[category] = {'category_count': 1, 'price': price}

        return result
        
        
    def find(self, product_id):
        rows = self._connection.execute(
            'SELECT * from products WHERE id = %s', [product_id])
        
        if rows:
            row = rows[0]
            return Product(row['id'], row['product_name'], row['quantity'], row['category'], row['price'], row['user_id'])
        else:
            return None

    
    def create(self, product):
        rows = self._connection.execute('INSERT INTO products (product_name, quantity, category, price, user_id) VALUES (%s, %s, %s, %s, %s) RETURNING id', [
                                        product.product_name, product.quantity, product.category, product.price, product.user_id])
        
        row = rows[0]
        product.id = self._generate_next_id()
        product.id = row["id"]
        return product 

    
    def delete(self, id):
        self._connection.execute(
            "DELETE FROM products WHERE id = %s",
            [id]
        )
        return None
    
    
    # ensure that the nex id always the +1 from the latest created.     
    def _generate_next_id(self):
        users = self.all()
        return max([user.id for user in users], default=0) + 1