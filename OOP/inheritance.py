# base/super/parent class
# inheritance is the process by which one class takes
# on the attributes and functions of a parent class
class Employee:

    def __init__(self, name, age, level, salary):
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    def work(self):
        print(f'{self.name} is working...')


# child class, inherits, extends, and overrides base class
class SoftwareEngineer(Employee):

    def __init__(self, name, age, level, salary, languages):
        # call initializer of parent class
        super().__init__(name, age, level, salary)
        # extend the parent class attributes
        self.languages = languages

    # extend the parent class functionality
    def debug(self):
        print(f'{self.name} is debugging code...')

    # override the parent class functionality
    def work(self):
        print(f'{self.name} is coding...')


class Designer(Employee):

    # override the parent class functionality
    def work(self):
        print(f'{self.name} is designing...')

    #  extend the parent class functionality
    def draw(self):
        print(f'{self.name} is drawing...')


if __name__ == 'main':

    se = SoftwareEngineer('Tom', 38, 'senior', 31500, ['c#', 'python', 'js'])
    de = Designer('Bob', 25, 'middleweight', 27500)

    se.work()
    de.work()
