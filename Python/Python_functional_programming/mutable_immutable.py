# function containing side effect
def add_to_list(l):
    l.append(5)

l = []

add_to_list(l)
print(l)

add_to_list(l)
print(l)

# clear function "add"

def add_to_list(l):
    return l + [5]

l = []

l1 = add_to_list(l)
print(l1)

l2 = add_to_list(l)
print(l2)