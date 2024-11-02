def pretty_args(args):
    return ", ".join([repr(arg) for arg in args])


def pretty_kwargs(kwargs):
    return ", ".join([
        f"{key}={repr(value)}"
        for key, value in kwargs.items()
    ])


def pretty_func(func, args, kwargs):
    args_str = pretty_args(args)
    kwargs_str = pretty_kwargs(kwargs)
    if args_str and kwargs_str:
        return args_str, kwargs_str
    return f"{args_str or kwargs_str}"


def recviz(func):
    recursion_level = 1
    
    def wrapper(*args, **kwargs):
        nonlocal recursion_level
        func_str = pretty_func(func, args, kwargs)
        whitespace = "    " * (recursion_level - 1)
        print(f"{whitespace}-> {func.__name__}(", end='')
        print(*func_str, sep=', ', end=')\n')
        
        recursion_level += 1
        return_value = func(*args, **kwargs)
        recursion_level -= 1
        print(f"{whitespace}<- {repr(return_value)}")
      
        return return_value
    
    return wrapper
