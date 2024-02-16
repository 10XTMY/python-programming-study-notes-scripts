# errors and exceptions

# import somemodule  # module not found error
# a = 5 + 'string'  # type error
# b = c  # name error, c undefined
# f = open('somefile.txt')  # file not found error
a = [1, 2, 3]
# a.remove(4)  # value error when a function is passed the right type but incorrect value
# b = a[5]  # index error, out of range
my_dict = {'name': 'Max'}
# my_dict['age']  # key error, age not in dictionary

# raising exceptions
x = -5
# x = 5
# if x < 0:
#     raise Exception('x should be positive')

# assertions throw error if not true
# assert (x >= 0), 'x should be positive'

# handling exceptions
try:
    a = 5 / 0  # zero division error
    b = 5 + '10'  # type error
except ZeroDivisionError as error:
    print(error)
except TypeError as error:
    print(error)
else:  # runs if no exceptions
    print('everything is fine')
finally:  # runs always regardless of exceptions
    print('cleaning up')


# define custom error classes by subclassing from base exception class
class ValueTooHighError(Exception):
    pass


class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_value(value):
    if value > 100:
        raise ValueTooHighError('value is too high')
    if value < 5:
        raise ValueTooSmallError('value is too small', value)


try:
    test_value(200)
except ValueTooHighError as error:
    print(error)

try:
    test_value(500)
except ValueTooSmallError as error:
    print(error.message, error.value)
except ValueTooHighError as error:
    print(error)
