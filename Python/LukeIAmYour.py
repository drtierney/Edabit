def relation_to_luke(name):
	relation = {
		"Darth Vader" : "father",
		"Leia"        : "sister",
		"Han"         : "brother in law",
		"R2D2"        : "droid"
	}
	
	return "Luke, I am your {0}.".format(relation.get(name))