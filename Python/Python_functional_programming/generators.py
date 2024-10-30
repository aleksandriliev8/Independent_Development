def generate_nth_perfect_square(n):
    return (n-1) ** 2

print(generate_nth_perfect_square(3))


def generate_all_perfect_squares_until(n):
    result = []
    for i in range(1, n + 1):
        result.append(generate_nth_perfect_square(i))
    
    return result

print(generate_all_perfect_squares_until(5))

# example of generator
def perfect_squares(n):
    for i in range(1, n+1):
        yield generate_nth_perfect_square(i)

# prints generator object
print(perfect_squares(5))

for i in perfect_squares(5):
    print(i)

# endless loop for finding perfect squares
def perfect_square():
    n = 1
    while True:
        yield generate_nth_perfect_square(n)
        n += 1

# 
perfect_squares_generator_exp = (generate_nth_perfect_square(i) for i in range(1, 6))

print(perfect_squares_generator_exp)
print(next(perfect_squares_generator_exp))
print(next(perfect_squares_generator_exp))
print(next(perfect_squares_generator_exp))

perfect_squares_n_generator_exp = lambda n: (generate_nth_perfect_square(i) for i in range(1, n + 1))

for num in perfect_squares_n_generator_exp(3):
    print(num)

print('--')
for num in perfect_squares_n_generator_exp(10):
    print(num)