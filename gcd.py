import math

def gcd(a, b):
	if a < b:
		c = a
		a = b
		b = c
	remainder = b
	while remainder > 0:
		a = b
		b = remainder
		remainder = a % b
	return b

def extendedGcd(a, b):
	swap = False
	if a < b:
		c = a
		a = b
		b = c
		swap = True
	newRemainder = b
	remainder = a
	oldRemainder = a
	u = 0
	v = 1
	oldU = 1
	oldV = 0
	multiplier = 1
	while newRemainder > 0:
		oldRemainder = remainder
		remainder = u * a + v * b
		multiplier = oldRemainder / remainder
		multiplier = math.floor(multiplier)
		remainder
		newRemainder = oldRemainder - remainder * multiplier
		newU = u * (- multiplier) + oldU
		oldU = u
		u = newU
		newV = v * (- multiplier) + oldV
		oldV = v
		v = newV
	if swap:
		c = oldU
		oldU = oldV
		oldV = c
	return (remainder, oldU, oldV)

