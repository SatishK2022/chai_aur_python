# Problem: Create a decorator to print the function name and the values of its arguments every time the function is called.

def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k}:{v}" for k, v in kwargs.items())
        print(f"calling: {func.__name__} with args {args_value if len(args_value) > 0 else 0 } and kwargs {kwargs_value if len(kwargs_value) > 0 else 0}")
        return func(*args, **kwargs)
    return wrapper

@debug
def greet(name, h, greeting="Hello"):
    print(f"{greeting}, {name}, {h}")

@debug
def hello():
    print("Hello")


hello()
greet("Satish", "gw", greeting="Hanji")