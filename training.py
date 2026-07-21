def logger(func):
    def wrapper(name):
        print("Before Function")

        result = func(name)

        print("After Function")

        return result

    return wrapper


def greet(name):
    print(name)


greet = logger(greet)
greet("naveen")
