# class decorators do the same thing as function decorators but are typically used to maintain and update a state
# keep track of how many times a function is executed
# time executions, register functions like plugins, cache return values, add information, update state etc

class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):  # allows you to execute class as a function
        self.num_calls += 1
        print(f'This has been executed {self.num_calls} times')
        return self.func(*args, **kwargs)

# cc = CountCalls(None)
# cc()


@CountCalls
def say_hello():
    print('Hello')


say_hello()
say_hello()
say_hello()
