import sys
import timeit

# sets are unordered, mutable (unchangeable elements but can add and remove), and do not allow duplicates
my_set = set('Hello')
print(my_set)  # notice only one l, good for quickly finding unique values in lists, tuples..

my_set.add(2)
print(my_set)

# if you use .remove() and the element does not exist a key error will be raised
# so use .discard() instead and no error will be raised if element not present
my_set.discard(2)
print(my_set)

# pop will return an arbitrary value and removes it
print(my_set.pop())
print(my_set)

# iterate as normal
for i in my_set:
    print(i)

if 2 in my_set:
    print('yes')
else:
    print('no')

set_a = {1, 2, 3, 4, 5, 6}
set_b = set_a.copy()  # or set(set_a)

# frozen set, immutable version of a normal set
frozen_set = frozenset([1, 2, 3, 4, 5, 6])

print(set_a, type(set_a))
print(frozen_set, type(frozen_set))

# set_a.add(2)
# frozen_set.add(2)  # error, however union, intersection, difference, and symmetric still work

# union, intersection, difference, and symmetric
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

# returns a set with all elements of both sets
union_set = odds.union(evens)
print(union_set)

# returns a set with the elements contained in both
intersection_set = odds.intersection(evens)
print(intersection_set)  # empty

intersection_set = odds.intersection(primes)
print(intersection_set)  # all odd numbers in both

intersection_set = evens.intersection(primes)
print(intersection_set)  # all even numbers in both

# returns elements from the first set that are not in the second set
difference_set = odds.difference(primes)
print(difference_set)

# returns a set with all the elements from both sets but not the elements that are in both
symmetric_difference_set = odds.symmetric_difference(primes)
print(symmetric_difference_set)

# to modify sets in place as opposed to returning a new one:
odds.update(evens)
print(odds)
odds = {1, 3, 5, 7, 9}
odds.intersection_update(primes)
print(odds)
odds = {1, 3, 5, 7, 9}
odds.difference_update(primes)
print(odds)
odds = {1, 3, 5, 7, 9}
odds.symmetric_difference_update(primes)
print(odds)
odds = {1, 3, 5, 7, 9}

# subset, superset, and disjoint
set_a = {1, 2, 3, 4, 5, 6}
set_b = {1, 2, 3}
set_c = {8, 9, 10}
# subset return True if all elements of first set are in second set
print(set_a.issubset(set_b))
# superset returns True if all elements in second set are in first set
print(set_a.issuperset(set_b))

# disjointed returns True if both sets have no similar elements
print(set_a.isdisjoint(set_b))
print(set_a.isdisjoint(set_c))

# memory consumption
my_tuple = (1, 2, 3, 4, 5, 6)
my_list = [1, 2, 3, 4, 5, 6]
print('set: ', set_a, sys.getsizeof(set_a), 'bytes')
print('list: ', my_list, sys.getsizeof(my_list), 'bytes')
print('tuple: ', my_tuple, sys.getsizeof(my_tuple), 'bytes')

# speed of creating a tuple vs a list vs set 1 million times
print('set time: ', timeit.timeit(stmt='{0, 1, 2, 4, 5}', number=1000000))
print('list time: ', timeit.timeit(stmt='[0, 1, 2, 4, 5]', number=1000000))
print('tuple time: ', timeit.timeit(stmt='(0, 1, 2, 4, 5)', number=1000000))

# time taken to iterate and increase each value by 1, 1 million times
print('iterating sets: ', timeit.timeit(stmt='for i in {0, 1, 2, 4, 5}: i+=1', number=1000000))
print('iterating lists: ', timeit.timeit(stmt='for i in [0, 1, 2, 4, 5]: i+=1', number=1000000))
print('iterating tuple: ', timeit.timeit(stmt='for i in (0, 1, 2, 4, 5): i+=1', number=1000000))
