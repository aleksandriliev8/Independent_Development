# function as object
def multiply(a, b):
    return a * b

f = multiply

print(f(2,3))


# function as parameter

def sum_(a, b) :
    return a + b

def apply_to_numbers(a, b, f):
    print(f'Applying a function to {a} and {b}')
    return f(a, b)

print(apply_to_numbers(2, 3, sum_))
print(apply_to_numbers(2, 3, multiply))

# returning function as a result from 
# another function

def foo():
    print("Foo called")

def bar():
    return foo

# f is an object who points to
# the result of bar() -> foo()
f = bar()
f()

# defining a function in the body of another
def foo():
    def bar():
        print("Bar called")
    
    return bar

f = foo()
f() 

# example logging function
def log_and_run(f, args=(), kwargs={}):
    print(f'Calling {f} with {args} and {kwargs}')
    return f(*args, **kwargs)

def add(a, b):
    return a+ b

print(log_and_run(add, (2, 3)))

# functions in dictionary and lists

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

actions = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

first = input('Enter a number: ')
operation = input('Enter an operation (+, -, * or /)')
second = input('Enter a number: ')

if operation not in actions:
    print('Operation not supported')
else:
    if not first.isnumeric() or not second.isnumeric():
        print('Input is not a number')
    else:
        first = int(first)
        second = int(second)

        result = actions[operation](first, second)
        print(f'{first} {operation} {second} = {result}')