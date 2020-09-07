def how_manny_leaves(tree_type,N):
	branches = {'big tree' : 100, 'medium tree' : 50, 'small tree': 25}
	
	return branches.get(tree_type) * N