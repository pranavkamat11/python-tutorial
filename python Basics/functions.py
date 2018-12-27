# hello function

def say_hello():
	print("hello world")

say_hello()


# learning about default arguments . Here name 'You' is default if we don't pass any name argument while calling the function
def hello_func(greeting,name='You'):
	return '{},{}'.format(greeting,name)

print(hello_func('Hi',name = 'Anderson'))

# args and kwargs

def student_info(*args, **kwargs):
	print(args)
	print(kwargs)


student_info("Science","Maths",name="Pranav",age=12)
print("hello man break")
courses = ['Science', 'Maths']
info = {'name': 'Pranav', 'age': 12}
student_info(*courses,**info)
