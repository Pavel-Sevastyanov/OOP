import sys

cards = [el.strip() for el in sys.stdin]
result = len(cards) - len(set(cards))
print(result)
