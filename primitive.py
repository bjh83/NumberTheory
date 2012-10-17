#Finds primitive roots
def primitives(prime):
	toCheck = 2
	primitives = []
	currentPower = 1
	while toCheck < prime:
		while currentPower < prime:
			if pow(toCheck, currentPower) % prime == 1:
				if currentPower == prime - 1:
					primitives.append(toCheck)
				else:
					break
			currentPower += 1
		currentPower = 1
		toCheck += 1
	return primitives

