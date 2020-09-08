def fix_import(s):
	line = s.split(" ")
	return "from {0} import {1}".format(line[3], line[1])