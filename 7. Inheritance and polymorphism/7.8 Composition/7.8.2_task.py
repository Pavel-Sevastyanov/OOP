class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name}, {self.price}$'


class ShoppingCart:
    def __init__(self, items=[]):
        self.items = list(items)

    def add(self, item):
        self.items.append(item)

    def total(self):
        return sum(item.price for item in self.items)

    def remove(self, name_item):
        self.items = [item for item in self.items if item.name != name_item]

    def __str__(self):
        result = list(map(lambda item: str(item) + '\n', self.items)) if self.items else ''
        return f'{"".join(result).rstrip()}'