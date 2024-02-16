# collections: counter, namedtuple, ordereddict, deque, defaultdict
from collections import Counter, namedtuple, OrderedDict, deque, defaultdict


a = 'aaaaabbbbccc'
# creates a dictionary with the value as key and the count as the value pair
my_counter = Counter(a)
print(my_counter)
# returns a list of the keys
print(my_counter.keys())
# returns a list of the values
print(my_counter.values())
# returns a list of all elements
print(list(my_counter.elements()))

# returns most common elements as a list of tuples
print(my_counter.most_common())
# returns first most common element in a list of tuples
print(my_counter.most_common(1))
# returns the first most common element tuple
print(my_counter.most_common(1)[0])
# returns the first most common element tuple value at index 0
print(my_counter.most_common(1)[0][0])

# namedtuple
# creates a class called Point with the fields x and y
Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt)
print(pt.x, pt.y)

# ordered dictionary
# just like a regular dictionary but remembers the order the items were added
# since python 3.7 this is standard for dict, so it has become redundant
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)

# default dictionary
# same as normal but has a default value if the key has not been set
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
d['a'] = 3
print(d['c'])  # returns value of 0 which is default value of int instead of raising an error

# deque
# deque is a double ended queue used to add or remove elements from both ends
my_deque = deque()
# default append always adds to the end, or the right
my_deque.append(1)
my_deque.append(2)
print(my_deque)
# append left appends to the front
my_deque.appendleft(3)
print(my_deque)
# pop removes and/or returns the last element
my_deque.pop()
print(my_deque)
# popleft removes and/or returns the first element
my_deque.popleft()
print(my_deque)
# extend adds all elements to the right, end
my_deque.extend([4, 5, 6])
print(my_deque)
# extend left adds all elements to the left, front
my_deque.extendleft([4, 5, 6])
print(my_deque)
# rotates all elements n place to the right
my_deque.rotate(1)
print(my_deque)
# rotates all elements n place to the left
my_deque.rotate(-1)
print(my_deque)

