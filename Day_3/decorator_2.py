def decorator_fn(func):
    def wrapper(a, b):
        if(b > a):
            a, b = b, a
        return func(a,b)
    return wrapper


@decorator_fn
def add(a : int, b : int) -> float:
    return a / b

print(add(20,100))