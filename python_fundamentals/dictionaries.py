# dictionaries are key-value pairs, unordered, and mutable
my_dict = {'name': '10XTMY', 'age': 99, 'location': 'London'}
my_dict_b = dict(name='10XTMY', age=99, location='London')
print(my_dict, my_dict_b)

# accessing values by key
value_a = my_dict['name']
print(value_a)

# add mew key value pair
my_dict['email'] = 'tom@tom.com'
print(my_dict)

# delete pairs
del my_dict['name']
print(my_dict)

# pop
age = my_dict.pop('age')
print(age)

# pop item returns last added pair
popped_item = my_dict.popitem()
print(popped_item)
print(my_dict)

# clear entire dictionary
my_dict.clear()
print(my_dict)
my_dict = {'name': '10XTMY', 'age': 99, 'location': 'London'}
print(my_dict)

if 'name' in my_dict:
    print(my_dict['name'])

# or
try:
    print(my_dict['lastname'])
except:
    print('error, key not in dictionary')

# loop through the keys and values
for key in my_dict.keys():
    print(key)
for value in my_dict.values():
    print(value)
for key, value in my_dict.items():
    print(key, value)

# copy a dictionary
my_dict_copy = my_dict.copy()

# merge two dictionaries
my_dict_c = dict(name='Sara', age=30, location='London')
my_dict_d = dict(name='10XTMY', age=99, location='London', email='10XTMY@10XTMY.com')

my_dict_c.update(my_dict_d)
print(my_dict_c)

# can use numbers or tuples as key types
# lists cannot be used as they are not hashable due to being mutable
my_dict_e = {3: 9, 6: 36, 9: 81}
print(my_dict_e)

my_tuple = (8, 7)
mydict_f = {my_tuple: 15}
print(mydict_f)
