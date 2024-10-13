def quantity(iterable, predicate):
    return sum(1 for el in filter(predicate, iterable))