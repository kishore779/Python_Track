import functools


def my_decorator(func):
    @functools.wraps(func)  # Preserves the original function's name and metadata
    def wrapper(*args, **kwargs):
        # 1. Do something BEFORE the original function runs
        print("Something is happening BEFORE the function is called.")

        # 2. Execute the original function and capture its output
        result = func(*args, **kwargs)

        # 3. Do something AFTER the original function runs
        print("Something is happening AFTER the function is called.")

        # 4. Return the result so the original function's output isn't lost
        return result

    return wrapper


# --- How to Use It ---


@my_decorator
def greet(name):
    print(f"Hello, {name}!")
    return f"Greeted {name}"


# Call the decorated function
response = greet("Alice")
print(f"Function Return Value: {response}")
