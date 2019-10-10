"""
Created on Wed Sep 11 22:30:55 2019

Dictionary
"""

# Dictionary is a data structure that stores data in key-value pairs
# key and values can be any data type - str, int

student = {'name': 'John', 'age' : 25, 'courses' : ['math', 'science']}

print(student['courses']) #accessing value of a key
#print(student['phone']) #raises Key error as the key does not exist

# using the get method we can define the default value of the key that do not exist
print(student.get('name')) 
print(student.get('phone')) # returns NONE instead of key error
print(student.get('phone', 'Not Found')) # error message changed from NONE to NOT FOUND

student['phone'] = '555-555' # new key
student['name'] = 'Jane' #updating a key value

# to update multiple key values
student.update({'name':'Jane', 'age': 26, 'phone': '555-555'})

# delete specific key value
del student['age'] #method 1
#age = student.pop('age') #method 2: removes 'age' from dictionary but stores its value in a variable

len(student) # to see how many keys
print(student.keys()) # all keys
print(student.values()) # all values
print(student.items()) # all key-value pairs

# looping through keys
for key in student:
    print(key)
    
# looping through both key and value
for key, value in student.items():
    print(key, value)

#%%