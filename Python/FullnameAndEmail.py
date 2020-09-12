class Employee:
	def __init__(self, firstname, lastname):
		self.firstname = firstname
		self.lastname = lastname
		# Complete the code!
		self.fullname = "{0} {1}".format(firstname, lastname)
		self.email = "{0}.{1}@company.com".format(firstname, lastname).lower()