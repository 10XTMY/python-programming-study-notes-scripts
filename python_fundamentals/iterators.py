# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators
import operator
from itertools import product, permutations, combinations, accumulate, groupby, combinations_with_replacement, \
    count, cycle, repeat


# iterate using enumerate instead of a range(len())
data = [1, 2, -4, -5]
# for i in range(len(data)):
#     if data[i] < 0:
#         data[i] = 0

for idx, val in enumerate(data):
    if val < 0:
        data[idx] = 0

# product returns an iterator that returns the cartesian product
a = [1, 2]
b = [3, 4]
prod = product(a, b)
print(list(prod))
a = [1, 2]
b = [3]
prod = product(a, b, repeat=2)
print(list(prod))

# permutations returns an iterator that returns all possible orderings of an input
a = [1, 2, 3]
perm = permutations(a)
print(list(perm))
# specify the length of permutations
perm = permutations(a, 2)
print(list(perm))

# combinations returns an iterator that returns all possible combinations of an input
# no combinations of the same arguments (to do this use combinations_with_replacement)
a = [1, 2, 3]
comb = combinations(a, 3)  # provide length of combination, in this case 3
print(list(comb))
comb_wr = combinations_with_replacement(a, 3)
print(list(comb_wr))

# accumulate returns an iterator that returns accumulated sums or any other binary function given as input
a.append(4)
acc = accumulate(a)
print(a)
print(list(acc))
# provide a function to accumulate
acc = accumulate(a, func=operator.mul)
print(list(acc))
a = [1, 2, 5, 3, 4]
acc = accumulate(a, func=max)
print(list(acc))


# groupby returns an iterator that returns keys and group iterators as value pairs


def smaller_than_3(x):
    return x < 3


a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_3)
print(group_obj)

for key, value in group_obj:
    print(key, list(value))

# can also use a lambda function here
group_obj = groupby(a, key=lambda x: x < 3)
for key, value in group_obj:
    print(key, list(value))

persons = [{'name': 'Tom', 'age': 38},
           {'name': 'Bob', 'age': 20},
           {'name': 'Jill', 'age': 20},
           {'name': 'Susan', 'age': 38}]

group_obj = groupby(persons, key=lambda x: x['age'])
for key, value in group_obj:
    print(key, list(value))

# infinite loop that starts at 10 and keeps adding one
for i in count(10):
    print(i)
    if i == 15:
        break

# infinite loop that cycles an input over and over again
a = [2, 3, 4]
for i in cycle(a):
    print(i)
    break

# infinite repetition unless stop parameter given
for i in repeat(1, 4):
    print(i)
