class Product:
    def __init__(self,id, product_name, quantity, category):
        self.id = id
        self.product_name = product_name 
        self.quantity = quantity
        self.category = category
        
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Product({self.id}, {self.product_name}, {self.quantity}, {self.category})"