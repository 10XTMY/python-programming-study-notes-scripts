
def foo(a, b, c):  # parameters
    print(a, b, c)


foo(1, 2, 3)  # positional arguments
foo(a=1, b=2, c=3)  # keyword arguments (much clearer/readable, use keyword arguments!)


# default arguments
def foob(a, b, c, d=4):  # default arguments must be at the end of the functional parameters
    print(a, b, c, d)


foob(a=1, b=2, c=3)
foob(a=1, b=2, c=3, d=8)  # override default argument


# *args and **kwargs
def foobargs(a, b, *args, **kwargs):  # *args =  tuple, **kwargs is a dictionary
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])


print('\nfoobargs:')
foobargs(1, 2, 3, 4, 5, six=6, seven=7)
foobargs(1, 2, 3, 4, 5)
foobargs(1, 2, six=6, seven=7)


# forced keyword arguments
def foo_forced(a, b, *, c, d):  # after * must be a keyword argument
    print(a, b, c, d)


def foo_forced_b(*args, last):  # last must be a keyword argument
    for arg in args:
        print(arg)
    print(last)


print('\nfoo_forced:')
foo_forced(1, 2, c=3, d=4)
foo_forced_b(1, 2, 3, last=4)


# unpacking arguments
def foo_unpack(a, b, c):
    print(a, b, c)


# length of container must match amount of parameters in function
my_list = [0, 1, 2]
my_tuple = (0, 1, 2)
my_dict = {'a': 1, 'b': 2, 'c': 3}  # keys must match parameter names as defined in function
foo_unpack(*my_list)
foo_unpack(*my_tuple)
foo_unpack(**my_dict)


# local vs global variables
def foo_local_v_global():
    global number
    x = number  # local variable x
    number = 3  # global variable number is changed from within function
    print(f'number inside the function {x}')


print('\nlocal vs global:')
number = 0
foo_local_v_global()
print(number)


# parameter passing: call by object or call by object reference
# parameter passed in is actually a reference to an object but the reference is passed by value
# there is a difference between mutable and immutable
# lists or dicts can be changed within a method but if rebinding the ref inside the func the outer reference will still
# point to the original object
# immutables like int or str cannot be changed within a function
# but immutable objects within a mutable object can be reassigned within a function
def foo_pass(x):
    x = 5  # automatically creates a local variable as it is immutable


def foo_pass_b(a_list):
    # a_list = [100, 200, 300]  # rebind the reference to a new list, no longer modifies outer object
    a_list.append(4)
    a_list[0] = 7
    a_list += [20, 40, 50]
    # a_list = a_list + [50, 100, 150]  # rebind the reference


print('\nparameter passing:')
var = 10
foo_pass(var)
print(var)

my_list = [1, 2, 3]
foo_pass_b(my_list)
print(my_list)  # original list is modified
