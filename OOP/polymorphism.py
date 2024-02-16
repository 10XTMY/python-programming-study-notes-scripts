from inheritance import SoftwareEngineer, Designer

employees = [SoftwareEngineer('Tom', 38, 'senior', 31500, ['c#', 'python', 'js']),
             SoftwareEngineer('Lisa', 25, 'junior', 22500, ['python', 'js']),
             Designer('Bob', 25, 'middleweight', 27500),
             Designer('Sara', 30, 'senior', 30000)]

# polymorphism is greek for 'many shapes'
# it enables to write code that works on child classes as though they were the parent class
# but still keeps the child class exactly as it is


def motivate_employees(employee_list):
    for employee in employee_list:
        print(f'Hey {employee.name}, there is a bonus for performance this month!')
        employee.work()


motivate_employees(employees)
