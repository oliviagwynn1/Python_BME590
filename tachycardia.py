tachycardic = ["tachycardic"] 

def is_tachycardic(candidate):
	strip = candidate.strip()
	case = strip.lower()
	space = case.replace(" ", "")
	for word in tachycardic:
		if word == strip:
			return True
		if word == case:
			return True
		if word == space:
			return True
	return False
	
			
