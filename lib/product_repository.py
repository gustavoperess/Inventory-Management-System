from lib.product import Product

class UserRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * from products')
        products = []
        for row in rows:
            product = Product(row['id'], row['product_name'], row['quantity'], row['category'])
            products.append(product)
        return products
    
        
    def find(self, product_id):
        rows = self._connection.execute(
            'SELECT * from products WHERE id = %s', [product_id])
        
        if rows:
            row = rows[0]
            return Product(row['id'], row['product_name'], row['quantity'], row['category'])
        else:
            return None

    
    def create(self, product):
        rows = self._connection.execute('INSERT INTO products (product_name, quantity, category) VALUES (%s, %s, %s) RETURNING id', [
                                        product.product_name, product.quantity, product.category])
        
        row = rows[0]
        product.id = self._generate_next_id()
        product.id = row["id"]
        return product 

    
    # ensure that the nex id always the +1 from the latest created.     
    def _generate_next_id(self):
        users = self.all()
        return max([user.id for user in users], default=0) + 1