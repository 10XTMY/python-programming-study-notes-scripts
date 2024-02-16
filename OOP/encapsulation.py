# encapsulation is the mechanism of hiding data implementation
# this means that instance variables are kept private and there
# is only one accessor method from outside (get, set)
# the same goes for methods

# use properties for getters and setters

class SoftwareEngineer:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # private/internal attributes
        # _salary = protected
        # __salary = private
        self.__salary = None
        self.__num_bugs_solved = 0

    def solve_bug(self):
        self.__num_bugs_solved += 1

    @property
    def num_bugs_solved(self):
        return self.__num_bugs_solved

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, base_value):
        self.__salary = self.__calculate_salary(base_value)

    @salary.deleter
    def salary(self):
        del self.__salary

    # private function (_calc = protected function)
    def __calculate_salary(self, base_value):
        if self.__num_bugs_solved < 10:
            return base_value
        if self.__num_bugs_solved < 100:
            return base_value * 2
        return base_value * 3


se = SoftwareEngineer('Tom', 38)

for i in range(20):
    se.solve_bug()

se.salary = 1000
print(se.num_bugs_solved)
print(se.salary)
del se.salary
try:
    print(se.salary)
except Exception as _err:
    print(f'error deleting se.salary: {_err}')


