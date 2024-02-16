# lists: ordered, mutable, allows duplicate elements
mylist = ['banana', 'cherry', 'apple']

# negative index, counting from the last item
print(mylist[-1])
print(mylist[-2])

# take last item out of the list and store in a new variable
# this removes it from the list
apple = mylist.pop()
print(apple)
print(mylist)

# add an item to the list
mylist.append(apple)
print(mylist)

# insert item at a specific index
mylist.insert(1, 'orange')
print(mylist)

# remove an item from the list
mylist.remove('orange')
print(mylist)

# remove all items
newlist = mylist.copy()
print(f'newlist: {newlist}')
newlist.clear()
print(f'newlist cleard: {newlist}')
print(mylist)

# reverse order the list
reveresed_list = mylist.reverse()
print(reveresed_list)
print(mylist)

# sort the list
number_list = [4, 3, 1, -1, -5, 10]
# number_list.sort()  # this sorts the list in place
sorted_list = sorted(number_list)  # this makes a sorted copy
print(sorted_list)
print(number_list)

# joining lists
mylist2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = mylist + mylist2
print(new_list)

# slicing
a = mylist2[1:5]  # from index 1 to 5
# if no index in front of the : it starts at beginning, if no index after the : it goes all the way to the end
# if no index is given and instead two :: then an index:
b = mylist2[::2]  # this returns whole list with a step of 2 (every second item)
c = mylist2[::-1]  # reverses the list
d = mylist2[:]  # this is equivalent to .copy()
e = mylist2[3:]
f = mylist2[:3]
print(a)
print(b)
print(c)
print(d)
print(f'e: {e}')
print(f'f{f}')

# to create a list of multiple of the same elements
new_list = [3] * 5
print(new_list)

# if I wanted to square the values in a list
e = [1, 2, 3, 4, 5, 6]
# expression first then the for loop iterating over the list
f = [i*i for i in e]
print(f)
