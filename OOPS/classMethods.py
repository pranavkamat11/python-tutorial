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

	@classmethod
	def from_string(cls,emp_str):
		first,last,pay = emp_str.split('-')
		return cls(first,last,pay) #cls(first,last,pay) will call the constructor

emp_1 = Employee('Pranav','Kamat',60000)
emp_2 = Employee('Gayatri','Kamat',50000)

emp_str_1 = 'John-Doe-70000'
new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.__dict__)

print(Employee.num_of_employees)