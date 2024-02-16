print(5 * 7)  # multiplication
print(2 ** 4)  # power (2 to the power of 4)
print([0] * 10)  # 10x zeros in a list
print([0, 1] * 10)  # list with repeated variables x10
print((0, 1) * 10)  # tuple with repeated variables x10
print('AB' * 10)  # string with 10x characters

# *args parameter is a tuple
# **kwargs parameter is a dictionary
# * as a parameter enforces keyword arguments after the *

# unpacking
# foo(*my_list) <- unpacks list into parameters, number of elements must match number of parameters
# foo(**my_dict) <- unpacks dictionary into parameters, number of elements must match number of parameters and keys
# must match name of parameters

numbers_list = [1, 2, 3, 4, 5, 6]
numbers_tuple = (1, 2, 3, 4, 5, 6)
*beginning, last = numbers_list  # unpacks all elements except last into a list, and last element into a single variable
*beginning, last = numbers_tuple  # unpacks into a list, regardless if original is a tuple
print(beginning, last)
beginning, *last = numbers_list  # unpacks first element into single variable, remaining into a list
print(beginning, last)
beginning, *middle, last = numbers_list  # unpacks the first and last into single variables, middle into a list
print(beginning, middle, last)

# merge into a list
my_tuple = (1, 2, 3)
my_list = [4, 5, 6]
my_set = {7, 8, 9}
new_list = [*my_tuple, *my_list, *my_set]
print(new_list)

# merge dictionaries
dict_a = {'a': 1, 'b': 2}
dict_b = {'c': 3, 'd': 4}
new_dict = {**dict_a, **dict_b}
print(new_dict)
