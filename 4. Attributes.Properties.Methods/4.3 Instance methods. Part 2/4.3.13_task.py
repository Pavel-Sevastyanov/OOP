class Postman:
    def __init__(self):
        self.delivery_data = []

    def add_delivery(self, street, house, flat):
        self.delivery_data.append((street, house, flat))

    def get_houses_for_street(self, street):
        adresses = dict.fromkeys(el[:2] for el in self.delivery_data)
        return [adress[1] for adress in adresses if adress[0] == street]

    def get_flats_for_house(self, street, house):
        adresses = dict.fromkeys(self.delivery_data)      
        return [adress[2] for adress in adresses if adress[0] == street and adress[1] == house]