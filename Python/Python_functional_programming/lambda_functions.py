lambda y: y + 1

(lambda a: print(a + 2)) (5)

# function assignment to a variable
f = lambda x: x + 1
print(f(5))

# function to compare objects 
# (in this case to sort the list from higher to lower)
l = [5, 2, 7, 3]
l.sort(key=lambda x: -x)
print(l)

# here first we sort the people by their age, then by their names
people_data = [('Ivan', 22), ('George', 71), ('Stilyana', 35), ('Dimitar', 51), ('Aleksandar', 35)]
people_data.sort(key=lambda person: (person[1], person[0]))
print(people_data)

# we can use it as well with sorted
people_data = [('Ivan', 22), ('George', 71), ('Stilyana', 35), ('Dimitar', 51), ('Aleksandar', 35)]
print(sorted(people_data, key=lambda person: (person[1], person[0])))