import sys
import timeit
# tuples are ordered, immutable, and allow duplicate elements
my_tuple = ('10XTMY', 99, 'London')
# parenthesis is optional, for a single item in a tuple must add a comma at the end: ('Tom',)

# use tuple function to create a tuple from an iterable:
my_tuple = tuple(['10XTMY', 99, 'London'])

# like lists tuples can be referenced by index
print(my_tuple[1])
print(my_tuple[-1])
# convert tuple to list
my_list = list(my_tuple)
print(my_list)
# my_tuple[1] = 'New' returns an error as tuples are immutable

for i in my_tuple:
    print(i)

if 'Tom' in my_tuple:
    print('yes')

my_tuple_b = ('a', 'p', 'p', 'l', 'e')

print(len(my_tuple_b))
# count the number of specified elements
print(my_tuple_b.count('p'))
# return the index of the first instance of specified element
print(my_tuple_b.index('p'))

# slicing works the same as lists
my_tuple_c = my_tuple_b[2:4]
my_tuple_d = my_tuple_b[::2]
print(my_tuple_c)
print(my_tuple_d)

# unpacking tuples
name, age, location = my_tuple
print(name, age, location)
print(type(name), type(age), type(location))

# unpack multiple elements with *
my_tuple_e = (0, 1, 2, 3, 4)
i1, *i2, i3 = my_tuple_e
print(i1, type(i1))  # first element
print(i2, type(i2))  # in between elements
print(i3, type(i3))  # last element

# because tuples are immutable python can make optimizations for speed
# this helps when using large amounts of data
print(my_tuple, sys.getsizeof(my_tuple), 'bytes')
print(my_list, sys.getsizeof(my_list), 'bytes')

# speed of creating a tuple vs a list x1 million
print('list time: ', timeit.timeit(stmt='[0, 1, 2, 4, 5]', number=1000000))
print('tuple time: ', timeit.timeit(stmt='(0, 1, 2, 4, 5)', number=1000000))

