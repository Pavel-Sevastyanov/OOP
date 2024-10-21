import re 

class PhoneNumber:
    def __init__(self, phone_number):
        self.phone_number = re.sub(r'(\d{3}) (\d{3}) (\d{4})', r'\1\2\3', phone_number)
       
    def __str__(self):
        return f'({self.phone_number[:3]}) {self.phone_number[3:6]}-{self.phone_number[6:]}'
    
    def __repr__(self):
        return f"PhoneNumber('{self.phone_number}')"