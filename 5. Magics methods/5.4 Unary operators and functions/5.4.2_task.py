class Money:
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f'{self.amount} руб.'

    def __pos__(self):
        return self.__class__(-self.amount) if self.amount < 0 else self.__class__(self.amount)

    def __neg__(self):
        return self.__class__(-self.amount) if self.amount > 0 else self.__class__(self.amount)            