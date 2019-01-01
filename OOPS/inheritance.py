class Employee :
	
	priority = "second"
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

class Developer(Employee):
	priority = "first"

# following automatically uses the parent class constructor
dev1 = Developer('panny','kamat',2345)
print(dev1.last)

# to get all inheritance info do following
print(help(Developer))

# normal inheritance 
print(dev1.pay)
print(dev1.apply_raise())
print(dev1.pay)
print(dev1.priority)

	


