from itertools import tee

def intersperse(iterable, delimiter):
    if iterable:
        iter_data = iter(iterable)
        a = next(iter_data)
        while True:
            try:
                yield a
                a = next(iter_data)
                yield delimiter
            except:
                break
