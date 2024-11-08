from contextlib import contextmanager
import sys
@contextmanager
def reversed_print():
    standart_out = sys.stdout.write

    sys.stdout.write = lambda text: standart_out(text[::-1])
    yield
    sys.stdout.write = standart_out