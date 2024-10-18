class Pet:
    pets = []
    def __init__(self, name):
        self.name = name

    @classmethod
    def first_pet(cls):       
        return cls.pets[0] if Pet.pets else None

    @classmethod
    def last_pet(cls):
        return cls.pets[-1] if Pet.pets else None

    @classmethod
    def num_of_pets(cls):
        return len(cls.pets)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        Pet.pets.append(self)
        self._name = name


