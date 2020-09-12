def grade_percentage(user_score, pass_score):
	s = 'FAILED' if user_score < pass_score else 'PASSED'
	return 'You {} the Exam'.format(s)