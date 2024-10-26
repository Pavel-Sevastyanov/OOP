class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __getattribute__(self, name):
        if name == 'name': 
            return object.__getattribute__(self, name).title()
        return object.__getattribute__(self, name)

    def __getattr__(self, name):
        if name == 'total': 
            return self.price * self.quantity
        raise AttributeError