tachycardic = ["tachycardic"] 

import string

def is_tachycardic(candidate):
	new_candidate = candidate.strip().lower().replace(" ", "")
	for word in tachycardic:
		if word == new_candidate:
			return True
		return False			
