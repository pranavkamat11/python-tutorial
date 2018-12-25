# List and tupples allow to work with sequential data

courses = ['history','Maths','computer']
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


courses = ['history','Maths','computer']
courses_2 = ["Machine Learning","Artificial Intelligence"]
courses.extend(courses_2)
print(courses)

courses = ['history','Maths','computer']
courses.remove('Maths')
print(courses)

# Using list like stack . ie removing the last element
courses = ['history','Maths','computer']
courses.pop()
print(courses)

# Set allows to work with collection of values with no duplicates