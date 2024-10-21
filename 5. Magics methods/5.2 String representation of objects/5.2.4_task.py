from functools import singledispatchmethod


class IPAddress:
    @singledispatchmethod
    def __init__(self, ipaddress: str):
        self.ipaddress = ipaddress
        
    @__init__.register(tuple)
    @__init__.register(list)
    def _from_sequence(self, ipaddress):
        self.ipaddress = '.'.join(map(str, ipaddress))
        
    def __str__(self):
        return self.ipaddress
    
    def __repr__(self):
        return f"IPAddress('{self.ipaddress}')"