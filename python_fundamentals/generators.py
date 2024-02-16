# functions that return an object that can be iterated over
# they generate the items lazily (one at a time only when requested), very memory efficient
# they are defined as a function but use the yield keyword instead of a return
import sys


def my_generator():
    yield 1
    yield 2
    yield 3


g = my_generator()

# for i in g:
#     print(i)

# print(sum(g))
#
# print(next(g))
# print(next(g))
# print(next(g))

# return a new list with all objects in a sorted order
sorted_list = sorted(g)
print(sorted_list)


def countdown(num):
    print('Starting countdown')
    while num > 0:
        yield num
        num -= 1


cd = countdown(4)
print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))


# great for handling large data
def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums


# returns a list which takes up large data
print(sum(firstn(1000000)))


def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1


print(sum(firstn_generator(1000000)))
print(f'size in bytes of list: {sys.getsizeof(firstn(1000000))}')
print(f'size in bytes of generator: {sys.getsizeof(firstn_generator(1000000))}')


def fibonacci(limit):
    # 0 1 1 2 3 5 8 13 ... first two are 0 and 1, all following are a sum of previous two
    # implement this as a generator:
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


fib = fibonacci(30)
for i in fib:
    print(i)

# generator expressions (similar to list comprehensions but using () instead of [])
my_generator = (i for i in range(10) if i % 2 == 0)  # all even elements from 0 to 9 into the generator
my_list = [i for i in range(10) if i % 2 == 0]
# print(list(my_generator))

for i in my_generator:
    print(i)

print(my_list)

my_generator = (i for i in range(100000) if i % 2 == 0)  # all even elements from 0 to 9 into the generator
my_list = [i for i in range(100000) if i % 2 == 0]
print(f'size of generator in bytes: {sys.getsizeof(my_generator)}')
print(f'size of list in bytes: {sys.getsizeof(my_list)}')
