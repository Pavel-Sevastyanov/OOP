from functools import wraps
import json

def jsonify(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = json.dumps(func(*args, **kwargs))
        return result
    return wrapper