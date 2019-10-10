"""
Created on Sat Sep  7 00:28:07 2019

Strings - variable, slicing, formatting, methods, concatenation
"""

# making a string variable
message = 'Hello World'

# when string contains '. Eg. Shreya's world
message = 'Shreya\'s World'
message = "Shreya's World"

# multi-line string
message = '''Hello World,
This is Shreya!'''
print(message)

# String is an array of individual charachters. We can access eash charachter
# through slicing
message = 'Hello World'
single_charachter = message[1]
many_charachters = message[1:5] #string[start:end]; start is inclusive while end is not
#index_out_of_range = message[11] # index error
index_2_onwards = message[2:]
till_index_3 = message[:4]

# finding length of string
length = len(message)

# All data types have certain methods associated with them. Method is a function
# which belongs to an object.
# String methods

lowercase = message.lower()
uppercase = message.upper()
count_charachter = message.count('l')
find_charachter = message.find('l') #return first index of occurence
not_found_charachter = message.find('z') 
replace_words = message.replace('World', 'Universe')

# String concatenation
greeting = 'Hello'
name = 'Reader'

new_message = greeting + name #output has no space between strings
new_message = greeting + ', ' + name
new_message = greeting + ', ' + name + '. How are you?' #difficult to keep track of all + 

# use string formatting which creates placeholder for each string
new_message = '{}, {}. How are you?'.format(greeting, name)

# another way is using fstrings (for python v3.6 and above)
new_message = f'{greeting}, {name}. How are you?'
#can use methods in fstrings
new_message = f'{greeting}, {name.upper()}. How are you?'

# Learn more about strings
print(dir(message)) # methods related to your string
help(str) # all string methods 
help(str.upper) # specific string method



#