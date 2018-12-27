language = 'Python'

# if else statements
if language == 'Python' :
	print("language is "+ language)
else:
	print("some different language")

# if elif else statements
language = 'Java'
if language == 'Python':
	print("language is pyhton")
elif language == 'Java':
	print("language is "+ language)
else:
	print("some different language")

if 3 > 2 :
	print("It indeed is greater")

# use of and or not
user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in :
	print('Admin has logged in')

logged_in = False
if not logged_in :
	print("Please log in")

a = [1,2,3]
b = [1,2,3]
print(a == b)
# a nd b are different in memory hence a is not b. their ids differ use function id(a) and id(b) and check
print(a is b)

# following a and b's address also would be same
a =[1,2,3]
b = a
print(a is b)

# in conditions [] , '' , {} evaluates to false