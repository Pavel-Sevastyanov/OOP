class Calculator:
    def __init__(self):
        pass
    
    def __call__(self, a, b, operation):
        if operation == '/' and not b:
            raise ValueError('Деление на ноль невозможно')
        return eval(str(a) + operation + str(b))