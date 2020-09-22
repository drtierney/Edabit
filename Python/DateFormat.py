def format_date(date):
	a = date.split("/")
	return "{0}{1}{2}".format(a[2], a[1], a[0])