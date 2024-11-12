from copy import deepcopy

class FieldTracker:
    def __init__(self):
        self.original_dict = deepcopy(self.__dict__)
        self.changed_dict = {}

    def base(self, attr):
        return self.original_dict[attr]

    def has_changed(self, attr):
        return self.__dict__[attr] != self.original_dict[attr]

    def changed(self):
        self.changed_dict = {attr: self.original_dict[attr] for attr in self.__class__.fields if self.has_changed(attr)}
        return self.changed_dict

    def save(self):
        self.original_dict = deepcopy(self.__dict__)        