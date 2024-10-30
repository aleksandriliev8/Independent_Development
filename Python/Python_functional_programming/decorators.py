def print_decorator(g):
    def inner():
        print("Hello")
        g()
    return inner

@print_decorator
def print_bye():
    print("bye")

print_bye()

# login example
def log(f):
    def inner(*args, **kwargs):
        print(f'Calling {f} with {args} and {kwargs}')
        return f(*args, **kwargs)
    return inner

@log
def add(a, b):
    return a + b

@log 
def subtract(a, b):
    return a - b

@log
def multiply(a, b):
    return a * b

@log
def divide(a, b):
    return a / b

print(add(2, 3))
print(subtract(3, 1))
print(multiply(1.5, b=3))
print(divide(a=12, b=6))

# runtime function timer example
import time

def time_it(f):
    def inner(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print(f'{f} took {end - start:.2f} seconds')
    return inner

@time_it
def slow_function(a):
    return (a ** a) ** a

slow_function(1000)