# there are two types of decorators, function and class

# a decorator allows you to add new functionality to an existing function without modifying the original
# functions in python are actually class objects, they can be defined inside another function, passed as arguments
# to a function and even returned by another function
import functools


# function decorators
def start_end_decorator(func):

    def wrapper():
        print('start')
        func()
        print('end')
    return wrapper


@start_end_decorator  # this decorator is equivalent of: print_name = start_end_decorator(print_name)
def print_name():
    print('Tom')


print_name()


# passing arguments
def start_end_decorator_args(func):
    @functools.wraps(func)  # passes the function __name__
    def wrapper(*args, **kwargs):
        print('start')  # do something before the function
        result = func(*args, **kwargs)
        print('end')  # do something after the function
        return result
    return wrapper


@start_end_decorator_args
def add5(x):
    return x + 5


print(add5(10))
print(help(add5))
print(add5.__name__)


# decorators can take arguments, 2 inner functions..
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat


@repeat(num_times=3)
def greet(name):
    print(f'Hello {name}')


greet('Tom')


# stacking decorators
def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f'{k}={v!r}' for k, v in kwargs.items()]
        signature = ', '.join(args_repr + kwargs_repr)
        print(f'calling {func.__name__}({signature})')
        result = func(*args, **kwargs)
        print(f'{func.__name__!r} returned {result!r}')
        return result
    return wrapper


@debug
@start_end_decorator_args
def say_hello(name):
    greeting = f'Hello {name}'
    print(greeting)
    return greeting


say_hello('Tom')
