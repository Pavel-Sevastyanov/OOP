class PiggyBank():
    content = 'coins'
    alternate_name = 'penny bank'


money_box = PiggyBank()

print(getattr(money_box, 'content'))
