def hash_function(obj):
    obj = str(obj)
    middle_index = len(obj) // 2
    temp1 = sum(ord(obj[i]) * ord(obj[~i]) for i in range(middle_index)) + (ord(obj[middle_index]) if len(obj) % 2 else 0)
    temp2 = sum(ord(obj[i]) * (i + 1) if not i % 2 else -ord(obj[i]) * (i + 1) for i in range(len(obj)))
    result = temp1 * temp2 % 123456791
    return result