# each method in class takes instance as the first argument
# below is converting regular method to class method
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

	@classmethod
	def set_raise_amt(cls,amount):
		cls.raise_amount = amount

emp_1 = Employee('Pranav','Kamat',60000)
emp_2 = Employee('Gayatri','Kamat',50000)
print("total number of employees is ")
print(Employee.num_of_employees)

Employee.set_raise_amt(1.5)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# even emp_1.set_raise_amt(1.6) works same unexpectadly