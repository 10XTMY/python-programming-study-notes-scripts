class SoftwareEngineer:

    # class attribute
    alias = 'Keyboard Magician'

    def __init__(self, name, age, level, salary):
        # instance attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    # instance method
    def code(self):
        print(f'{self.name} is writing code...')

    def code_in_language(self, language):
        print(f'{self.name} is writing code in {language}...')

    # dunder (double underscore) method
    def __str__(self):
        # returns string description of this class
        return f'name = {self.name}, age = {self.age}, level = {self.level}'

    def __eq__(self, other):
        # returns boolean of comparison of two instances of this class
        return self.name == other.name and self.age == other.age

    # class method
    @staticmethod
    def entry_salary(age):
        if age < 25:
            return 18000
        if age < 30:
            return 25000
        return 30000


# instantiate class
se1 = SoftwareEngineer('Tom', 38, 'Senior', 31500)
# use of instance method
se1.code_in_language('c#')
# use of class function
print(se1.entry_salary(20))
print(SoftwareEngineer.entry_salary(35))
