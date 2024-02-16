from functools import reduce


# lambda arguments: expression
add10 = lambda x: x + 10
print(add10(5))

mult = lambda x, y: x * y
print(mult(5, 5))

# sorted, map, filter, and reduce
points_2D = [(1, 2), (15, 1), (5, -1), (10, 4)]  # list of tuples

points_2D_sorted = sorted(points_2D)  # by default sorts by the first element of each tuple
print(points_2D)
print(points_2D_sorted)

points_2D_sorted = sorted(points_2D, key=lambda x: x[1])  # sorted by index 1 of x
print(points_2D_sorted)

points_2D_sorted = sorted(points_2D, key=lambda x: x[0] + x[1])  # sorted by the sum of x,y in each tuple
print(points_2D_sorted)

# map(func, seq)
a = [1, 2, 3, 4, 5]
b = map(lambda x: x * 2, a)
print(list(b))

# can achieve above with list comprehension
c = [x * 2 for x in a]
print(c)

# filter (func, seq) returns True or False, all elements for which the function evaluates to true
b = filter(lambda x: x % 2 == 0, a)  # returns even numbers
print(list(b))

# using list comprehension
c = [x for x in a if x % 2 == 0]
print(c)

# reduce (func seq) it repeatedly applies the function to the elements and returns a single value
# compute product of all elements example:
a = [1, 2, 3, 4]
product_a = reduce(lambda x, y: x*y, a)
print(product_a)
