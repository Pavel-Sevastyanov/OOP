import json

def jsonattr(filename):
    def decorator(cls):
        with open(filename, 'rt', encoding='utf-8') as file_attrs:
            attrs = json.load(file_attrs)
            for k, v in attrs.items():
                setattr(cls, k, v)
        return cls        
    return decorator