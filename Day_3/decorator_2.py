def decorator_fn(func):
    def wrapper(a, b):
        if b > a:
            a, b = b, a
        return func(a, b)

    return wrapper


@decorator_fn
def div(a: int, b: int) -> float:
    return a / b


@decorator_fn
def sub(a: int, b: int) -> int:
    return a - b


print(div(20, 100))
print(sub(2, -10))
