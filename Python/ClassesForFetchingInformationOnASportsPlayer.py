class player():

	def __init__(self, name, age, height, weight):
	# complete function
		self.name = name
		self.age = age
		self.height = height
		self.weight = weight
		
	def get_age(self):	
	# complete function
		return "{0} is age {1}".format(self.name, self.age)
		
	def get_height(self):	
	# complete function
		return "{0} is {1}cm".format(self.name, self.height)
		
	def get_weight(self):	
	# complete function
		return "{0} weighs {1}kg".format(self.name, self.weight)