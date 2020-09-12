def count_vowels(txt):
	count = 0
	vowels = 'aeiou'
	for c in txt.lower():
		if c in vowels:
			count += 1
	return count