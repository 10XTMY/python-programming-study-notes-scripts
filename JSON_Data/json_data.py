# javascript object notation, a lightweight data format

# Python                JSON
# dict                  object
# list, tuple           array
# str                   string
# int, long, float      number
# True                  true
# False                 false
# None                  null

import json
import pathlib
from json import JSONEncoder

person = {"name": "Tom", "age": 38, "city": "London", "hasChildren": False, "titles": ["developer", "programmer"]}

# serialization or encoding, convert dictionary to JSON

# dumps means dump into a string
person_json = json.dumps(person, indent=4, sort_keys=False)  # sort_keys sorts keys alphabetically
print(person_json)

# write to json file
with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)  # without indent=4 it will all be on one line

# deserialization or decoding, convert from json to dictionary

# load from string
person = json.loads(person_json)
print(person)

# load from file
with open('person.json', 'r') as file:
    person = json.load(file)
print(person)


# serialize a class to json
class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age


user_a = User('Tom', 38)
# user_json = json.dumps(user_a) <-- generates an error


# custom encoding function
def encode_user(x):
    if isinstance(x, User):
        return {'name': x.name, 'age': x.age, x.__class__.__name__: True}
    else:
        raise TypeError('object provided is not JSON serializable, object must be of type User')


# user_json = json.dumps(user_a, default=encode_user, indent=4, sort_keys=False)
user_json = encode_user(user_a)
print(user_json)
print(type(user_json))


# using json encoder class
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)


# first method
# user_json = json.dumps(user_a, cls=UserEncoder)
# user_json = dict(UserEncoder().encode(user_a))
# print(user_json)
# print(type(user_json))

# second method
# user_json = UserEncoder(indent=4, sort_keys=False).encode(user_a)
with open('user.json', 'w') as file:
    json.dump(user_json, file, indent=4, sort_keys=False)


# decode into a User class
def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct


with open('D:/Coding_Projects/my_tools/_practice/JSON_Data/user.json', 'r') as file:
    loaded_json = json.load(file)
    print(loaded_json)
    loaded_user = decode_user(loaded_json)
    print(loaded_user.age)
