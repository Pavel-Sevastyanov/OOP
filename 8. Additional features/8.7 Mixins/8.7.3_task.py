class AttributesMixin:
    def get_public_attributes(self):
        result = [
            (attr, value) for attr, value in self.__dict__.items() 
            if not attr.startswith('_')
            ]        
        return result

    def get_protected_attributes(self):
        result = [
            (attr, value) for attr, value in self.__dict__.items() 
            if attr.startswith('_') 
            and 
            self.__class__.__name__ not in attr
            ]        
        return result