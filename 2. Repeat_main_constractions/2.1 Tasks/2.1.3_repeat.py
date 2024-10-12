def check_right(seq):
    count = 0
    for el in seq:
        if el == '(':
            count += 1
        elif el == ')':
            count -= 1
        if count < 0:
            return False    
    return not bool(count)

print(check_right(input()))