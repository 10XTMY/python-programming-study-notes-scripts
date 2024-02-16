import random
import secrets
import numpy as np

# random should not be used for security purposes, for that use secrets module
# random generates pseudo random numbers, this means they are reproducible by setting a seed value
random.seed(1)

# random float
a = random.random()
print(a)

# random float within range
a = random.uniform(1, 10)
print(a)

# random int, upper bound is included
a = random.randint(1, 10)
print(a)

# random int, upper bound is not included
a = random.randrange(1, 10)
print(a)

# normalvariate useful working in statistics,
# picks a random value from a normal distribution,
# with a mean and standard deviation (mean=0, sd=1)
a = random.normalvariate(0, 1)
print(a)

# pick a random element from an input
my_list = list('ABCDEFGH')
a = random.choice(my_list)
print(a)

# pick n unique samples from an input
a = random.sample(my_list, 3)
print(a)

# pick n random elements including repeats
a = random.choices(my_list, k=3)
print(a)

# shuffle a list
random.shuffle(my_list)
print(my_list)

# secrets has three functions

# random int from 0-9
a = secrets.randbelow(10)
print(a)

# random bits, eg.. four random bits,  the highest value possible is 1111 (15)
# below will generate a random number from 0 to 15
a = secrets.randbits(4)
print(a)

my_list = list('ABCDEFGH')
# truly random choice that is not reproducible
a = secrets.choice(my_list)
print(a)

# working with arrays
# numpy uses a different random generator than the random module
# numpy also has its own seed function
np.random.seed(1)
a = np.random.rand(3, 3)  # random floats in a 3 by 3 array
print(a)

a = np.random.randint(0, 10, (3, 4))  # range from 0 to 9 in a 3 by 4 array
print(a)

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print(a)
np.random.shuffle(a)
print(a)
