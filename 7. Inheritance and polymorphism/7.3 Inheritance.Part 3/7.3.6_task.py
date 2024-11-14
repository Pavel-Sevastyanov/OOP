class RoundedInt(int):
    def __new__(cls, num, even=True):
        num += num % 2 if even else (num - 1) % 2
        return super().__new__(cls, num)