tachycardic = ["tachycardic"] 

import string

def is_tachycardic(candidate):
	punctuation = str.maketrans("", "", string.punctuation)
	new_candidate = candidate.strip().lower().replace(" ", "").translate(punctuation)
	for word in tachycardic:
		if word == new_candidate:
			return True
		else: 
			index = 0
			while index < len(new_candidate):
				letter = new_candidate[index]
				if letter == candidate[index]:
					return True
				elif letter == candidate[index + 1]:
					new_candidate = new_candidate.insert(index, candidate[index])
				return False
				index = index + 1
			if word == new_candidate:
				return True
			return False


	
	
