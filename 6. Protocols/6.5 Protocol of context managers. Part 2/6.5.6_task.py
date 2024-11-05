import sys

class UpperPrint:
    def upper_out(self, text):
        return self.standart_out(text.upper())

    def __enter__(self):
        self.standart_out = sys.stdout.write
        sys.stdout.write = self.upper_out

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout.write = self.standart_out