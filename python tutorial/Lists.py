# List and tupples allow to work with sequential data

courses = ['history','maths','computer']
print(courses)
print(len(courses))
print(courses[0])

# if list is too huge no need to worry about length use [-1]
print(courses[-1])

print(courses[0:2])
print(courses[1:])

courses.append('Art')
print(courses)
courses.insert(1,'geography')
print(courses)


courses = ['history','maths','computer']
courses_2 = ["Machine Learning","Artificial Intelligence"]
courses.extend(courses_2)
print(courses)

courses = ['history','maths','computer']
courses.remove('maths')
print(courses)

# Using list like stack . ie removing the last element
courses = ['history','maths','computer']
popped = courses.pop()
print(popped)

# reversing a list
courses = ['history','maths','computer']
courses.reverse()
print(courses)

#sorting the list 
courses = ['history','maths','computer']
courses.sort()
print(courses)

#sorting numbers
nums = [1,5,4,3]
nums.sort()
print(nums)

#sorting in descending order
nums = [1,5,4,3]
nums.sort(reverse = True)
print(nums)

# sorted function 
courses = ['history','maths','computer']
sorted_courses = sorted(courses)
print(sorted_courses)

# min function. similarly max function and sum 
nums = [1,5,4,3]
min_number = min(nums)
print(min_number)

# finding index 
courses = ['history','maths','computer']
print(courses.index('history'))

# check if something available in list
print('Docker' in courses)

# for loop to iterate through list 
courses = ['history','maths','computer']
for course in courses:
	print (course)

#getting index too while looping
courses = ['history','maths','computer']
for index , course in enumerate(courses):
	print(index , course , "line ",index + 1)

print("")

#setting start index too while looping
courses = ['history','maths','computer']
for index , course in enumerate(courses,start = 1):
	print(index , course)

# comma separation and all
courses = ['history','maths','computer']
courses_str = ', '.join(courses)
print(courses_str)

# converting comma separated or whatever string to list
new_list = courses_str.split(', ')
print(new_list)




# Set allows to work with collection of values with no duplicates