# strings are ordered, immutable, text representations
my_string = 'I\'m a coder'
print(my_string)

# strings are ordered, therefor indexed
char = my_string[0]
print(char)
char = my_string[:3]
print(char)

# immutable so cannot be changed
# my_string[3] = 'h'  # error

substring = my_string[1:5]  # starts at one until 4, excludes 5
print(substring)
substring = my_string[::2]
print(substring)

# concatenate
greeting = 'Hello'
name = 'Tom'
sentence = greeting + ' ' + name
print(sentence)

# iterate
# for i in greeting:
#     print(i)
#
# if 'ell' in greeting:
#     print('yes')

whitespace_string = '    H e l l o'
no_space_string = whitespace_string.strip()
print(whitespace_string)
print(no_space_string)

# strip leading and trailing characters present in the string but not in middle
print(greeting.strip('o'))
print(greeting.strip('l'))

# replace characters
print(greeting.replace('ll', ''))

# upper and lower case
upper_string = greeting.upper()
lower_string = greeting.lower()
print(upper_string, lower_string)

# endswith returns boolean
print(name.endswith('hello'))
print(name.endswith('m'))
print(name.endswith('Tom'))

# find first index of given char
print(greeting.find('l'))

# count how many chars in a string
print(greeting.count('l'))

# create list of words from a string
sentence_string = 'hey how are you?'
my_list = sentence_string.split()
print(my_list)

sentence_string = 'hey,how,are,you?'
my_list = sentence_string.split(',')
print(my_list)

# create a string from a list
string_from_list = ' '.join(my_list)
print(string_from_list)

# variables in strings

# old method
print('my name is %s' %name)
decimal_num = 3.2558214
print('the decimal is: %d' %decimal_num)
print('the float is: %f' %decimal_num)

# python < 3.6 method
print('the number is {}'.format(decimal_num))
print('the number is {:.2f}'.format(decimal_num))

# python >= 3.6 method
print(f'the number is {decimal_num}')
print(f'the number is {decimal_num:.2f}')
