class Product:
    def __init__(self,id, product_name, quantity, category, price, user_id):
        self.id = id
        self.product_name = product_name 
        self.quantity = quantity
        self.category = category
        self.price = price
        self.user_id = user_id
        
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Product({self.id}, {self.product_name}, {self.quantity}, {self.category}, {self.price}, {self.user_id})"