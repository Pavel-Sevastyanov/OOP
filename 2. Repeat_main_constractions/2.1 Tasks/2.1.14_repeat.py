def pluck(data, path, default=None):

    path = path.split('.') if '.' in path else [path]
    try:
        for key in path:
            if isinstance(data[key], dict):
                data = data[key] 
            else:
                return data[key]
        return data
    except:
        return default