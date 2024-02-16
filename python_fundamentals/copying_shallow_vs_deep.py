import copy

# shallow copy is one level deep, only copies references of nested child objects
# deep copy, full independent copy

original = 5
cpy = original  # new variable with same reference, not a real copy
cpy = 6  # creates a new variable with its own reference


original = [1, 2, 3]
cpy = original
cpy[0] = -10
print(cpy)
print(original)

# one level list
original = [1, 2, 3]
# all four below will make a shallow copy, one level deep
cpy = copy.copy(original)
# cpy = original.copy()
# cpy = list(original)
# cpy = original[:]
cpy[0] = -10
print(cpy)
print(original)

# nested list
original = [[1, 2, 3], [4, 5, 6]]
# cpy = copy.copy(original)  # will not work, original will be changed
cpy = copy.deepcopy(original)  # deep copy will work
cpy[0][1] = -10
print(cpy)
print(original)


# custom objects

# shallow
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person('Tom', 38)
person2 = copy.copy(person1)

person2.age = 39
print(person2.age)
print(person1.age)


# deep
class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee


person1 = Person('Tom', 38)
person2 = Person('Peter', 55)

company = Company(person1, person2)
company_clone = copy.deepcopy(company)

company_clone.boss.age = 56
print(company.boss.age)
print(company_clone.boss.age)
