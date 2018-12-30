# each method in class takes instance as the first argument
class Employee :
	
	num_of_employees = 0
	raise_amount = 1.4

	def __init__(self,first,last,pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first+'.'+last+'@company.com'
		Employee.num_of_employees += 1


	def fullname(self) :
		return '{} {}'.format(self.first,self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)
		# we can also access self.raise_amount

emp_1 = Employee('Pranav','Kamat',60000)
emp_2 = Employee('Gayatri','Kamat',50000)
print("total number of employees is ")
print(Employee.num_of_employees)
# printing whole data for emp_1. Actually self.raise_amount makes sense since the raise amount can be later different for different employees
print(emp_1.__dict__)

print(Employee.__dict__)

print(emp_1.email)

print(emp_1.fullname())
print(Employee.fullname(emp_1))
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
print(emp_1.raise_amount)
# emp_1.fullname() and Employee.fullname(emp_1) are same

# emp_1.raise_amount = 1.5
print(Employee.__dict__)
emp_1.raise_amount = 1.5

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(emp_2.pay)
emp_2.raise_amount = 1.8
emp_2.apply_raise()
print(emp_2.pay)
