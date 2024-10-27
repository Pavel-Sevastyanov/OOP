def limited_hash(left, right, hash_function=hash):
    def new_function(obj):
        result = hash_function(obj)
        while not (left <= result <= right):
            if result > right:
                result = left + (result - right - 1)
            if result < left:
                result = right - (left - result - 1)
        return result            
    return new_function