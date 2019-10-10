"""
Created on Tue Sep 10 20:19:22 2019

List, tuple and set
"""
# List
# a collection of elements from any data type (int, float, str) 
# mutable

courses = ['hindi', 'maths', 'science']

# accessing elements of a list
print(len(courses))
print(courses[0])
print(courses[2])
print(courses[-1])

# list methods - append, insert, extend, sort, reverse, min, max, sum
courses.append('art')
courses.insert(0, 'art') # the first argument indicates position

courses_2 = ['art', 'education']
courses.insert(0, courses_2) 
courses.append(courses_2) 
courses.extend(courses_2) #voila! removes square brackets in courses_2

courses = ['hindi', 'maths', 'science']
courses.reverse()
courses.sort()
courses.sort(reverse = True) #sorted in reverse order

# above methods alter the list in-place. To keep the original list intact, few methods
# are available that save the modified list in a new variable
sorted_courses = sorted(courses)

nums = [1, 2, 4, 5, 3, 10]
print(min(nums))
print(max(nums))
print(sum(nums))

# find index of certain value
print(courses.index('hindi'))
#print(courses.index('sports')) #Value Error! if index value does not exist

print('maths' in courses) 
print('sports' in courses)

# Looping using lists
for course in courses:
    print(course)
    
for index, course in enumerate(courses):
    print(index, course)
    
# joining and splitting list elements
course_str = ' - '. join(courses)
new_list = course_str.split(' - ')

# Tuples
# similar to list but immutable

# Mutable
list_1 = ['history', 'math', 'physics']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'art'

print(list_1)
print(list_2)

# Immutable
tuple_1 = ('history', 'math', 'physics')
tuple_2 = tuple_1

print(list_1)
print(list_2)

#tuple_1[0] = 'art' #Type error: 'tuple' object does not support item assignment

print(tuple_1)
print(tuple_2)

# Not many methods in tuple as of list as tuple cannot be modified

# if you want something that is mutable, use list.
# if you want something to just loop through and do not modify, use tuple

# Sets
# do not care about the order pf elements
# uses: 1) to remove duplicates 2) to check the existence of an element in a list

cs_courses = {'history', 'math', 'physics'}
cs_courses = {'history', 'math', 'physics', 'math'} #duplicate removed

# membership test to check the existence of element. Sets are much more efficient than tuple and
# list in this case
print('math' in cs_courses)

# set methods: intersection, difference, union
cs_courses = {'history', 'math', 'physics'}
art_courses = {'art', 'design', 'history'}

print(cs_courses.intersection(art_courses)) #common courses
print(cs_courses.difference(art_courses)) #courses in cs but not in art
print(cs_courses.union(art_courses)) #all courses

# Creating empty list, set, tuple

empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = {} #this is wrong! actually creates empty dictionary
empty_Set = set() #this is right!






























