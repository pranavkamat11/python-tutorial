student = {'name':'John','age':14,'courses':['Math','CompSci']}
print(student)
print(student['name'])
print(student['age'])
print(student.get('phone'))
print(student.get('age'))

# setting default value to the key which is not found
print(student.get('phone','Not Found'))
student['phone'] = '0832'
print(student['phone'])
# updating properties
student['name'] = 'Jane'
print(student)

# efficient way of updating
print("hello")
student = {'name':'John','age':14,'courses':['Math','CompSci']}
student.update({'name':'Jane','phone':'234'})
print(student)

# deleting age attribute
student = {'name':'John','age':14,'courses':['Math','CompSci']}
del student['age']
print(student)

# remove and capture key-value
age = student.pop('name')
print(age)

student = {'name':'John','age':14,'courses':['Math','CompSci']}
print(len(student))
print(student.keys())
print(student.values())


# if you want to see both keys and values
print(student.items())

# looping through key value pairs
for key , value in student.items():
	print(key,value)