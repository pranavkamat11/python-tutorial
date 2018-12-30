# each method in class takes instance as the first argument
class Employee :
	def __init__(self,first,last,pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first+'.'+last+'@company.com'

	def fullname(self) :
		return '{} {}'.format(self.first,self.last)
		

emp_1 = Employee('Pranav','Kamat',60000)

print(emp_1.email)

print(emp_1.fullname())
print(Employee.fullname(emp_1))

# emp_1.fullname() and Employee.fullname(emp_1) are same